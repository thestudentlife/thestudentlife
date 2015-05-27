from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from mainsite.models import Issue, Article, Section, Profile, AssignmentForm, FrontArticle, CarouselArticle, Copy, Photo
from workflow.models import Assignment, RegisterForm, LoginForm, Revision, ProfileForm, RegisterForm2, Comment
import os, subprocess,json
from workflow.static import getText

def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, '/workflow/denied/')

def deny(request):
    if request.user.is_anonymous():
        return redirect(reverse('login'))
    else:
        return render(request,'permission.html')

def get_old_profile(display_name):
    old_profile = None
    if Profile.objects.filter(display_name=display_name)!=0:
        profiles = Profile.objects.filter(display_name=display_name)
        for profile in profiles:
            if profile.user is None:
                old_profile = profile
    return old_profile

def register(request):
    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()
            display_name = user.first_name+" "+user.last_name
            position = request.POST['position']
            old_profile = get_old_profile(display_name)
            if old_profile:
                old_profile.user = request.user
                old_profile.save()
            else:
                profile = Profile(user=user,display_name=display_name,position=position)
                profile.save()
            user.set_password(request.POST['password'])
            user.save()
            plastic = Group.objects.get(name='plastic')
            bronze = Group.objects.get(name='bronze')
            user.groups.add(plastic)
            if not position == 'guest':
                user.groups.add(bronze)
            return redirect(reverse('whome'))
        else:
            return render(request, 'register.html', {
                'form': registerForm
            })
    else:
        registerForm = RegisterForm()
        return render(request, 'register.html', {
            'form': registerForm,
        })

def setting(request,user_id):
    if request.user.id != int(user_id):
        return render(request,'permission.html')
    user = User.objects.get(pk=user_id)
    if request.method=='GET':
        form = RegisterForm(instance=user)
        return render(request,'setting.html',{'form':form})
    else:
        form = RegisterForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return redirect(reverse('whome'))
        else:
            return render(request,'setting.html',{'form':form})




def login(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            do_login(request, user)
            next = request.GET.get('next')
            if next is None:
                return redirect(reverse('whome'))
            else:
                return HttpResponseRedirect(request.GET['next'])
        else:
            return render(request, 'login.html', {
                'form': loginForm
            })
    else:
        loginForm = LoginForm()
        return render(request, 'login.html', {
            'form': loginForm
        })

def logout(request):
    do_logout(request)
    return redirect(reverse('home'))

def whome(request):
    user = request.user
    latest = Issue.objects.latest('created_date')
    if user.is_anonymous():
        return redirect(reverse('login'))
    elif Group.objects.get(name='silver') in user.groups.all():
        return redirect(latest.get_absolute_url())
    elif user.profile.position == "photographer" or user.profile.position == "graphic_designer":
        photos = Photo.objects.filter(credit=request.user.profile)
        return render(request, 'bronze_whome.html', {'issue': latest, 'photos':photos})
    else:
        articles = request.user.profile.article_set.order_by('-created_date')
        return render(request, 'bronze_whome.html', {'issue': latest, 'articles': articles})

@group_required('gold')
def manage(request):
    users = User.objects.all()
    return render(request,'manage.html',{'users':users})

@group_required('gold')
def manage_one(request,user_id):
    user = User.objects.get(pk=user_id)
    if request.method=='GET':
        form = RegisterForm2(instance=user)
        second_form = ProfileForm(instance=user.profile)
        return render(request,'setting.html',{'form':form,'second_form':second_form})
    else:
        form = RegisterForm2(request.POST,instance=user)
        second_form = ProfileForm(request.POST,instance=user.profile)
        if form.is_valid():
            user = form.save()
        else:
            return render(request,'setting.html',{'form':form,'second_form':second_form})
        if second_form.is_valid():
            second_form.save()
        else:
            return render(request,'setting.html',{'form':form,'second_form':second_form})
        for group in user.groups.all():
            group.user_set.remove(user)
        for group in user.profile.ideal_group_names():
            group = Group.objects.get(name=group)
            user.groups.add(group)
        return redirect(reverse('manage'))

@group_required('silver')
def front(request):
    if request.method == "GET":
        latest_articles_for_front = list(Article.objects.order_by('-published_date')[:40])
        fronts = FrontArticle.objects.all()
        for front in fronts:
            if front.article in latest_articles_for_front:
                latest_articles_for_front.remove(front.article)
        latest_articles_for_carousel = list(Article.objects.order_by('-published_date')[:40])
        carousels = CarouselArticle.objects.all()
        for carousel in carousels:
            if carousel.article in latest_articles_for_carousel:
                latest_articles_for_carousel.remove(carousel.article)
        return render(request, 'front.html', {'latest_articles_for_front': latest_articles_for_front, 'fronts': fronts,
                                              'latest_articles_for_carousel': latest_articles_for_carousel,
                                              'carousels': carousels})
    else:
        FrontArticle.objects.all().delete()
        CarouselArticle.objects.all().delete()
        for id in request.POST.getlist("front_selected[]"):
            article = Article.objects.get(id=id)
            front = FrontArticle(article=article)
            front.save()
        for id in request.POST.getlist("carousel_selected[]"):
            article = Article.objects.get(id=id)
            carousel = CarouselArticle(article=article)
            carousel.save()
        return redirect(reverse('front'))

@group_required('bronze')
def article_xml(request, article_id):
    article = Article.objects.get(id=article_id)
    paragraphs = getText.dehtml(article.content).split('\n\n')
    data = render_to_string('articles/article_xml.xml', {'article': article, 'paragraphs': paragraphs})
    return HttpResponse(data, content_type='application/xml')

@group_required('silver')
def revision(request, pk):
    revision = Revision.objects.get(pk=pk);
    article = revision.article;
    index = list(article.revision_set.order_by('date')).index(revision)
    if index > 0:
        previous_revision_body = list(article.revision_set.order_by('date'))[index - 1].body
    else:
        previous_revision_body = ''
    file_1 = open('file_1', 'w')
    file_1.write(revision.body)
    file_1.close()
    file_2 = open('file_2', 'w')
    file_2.write(previous_revision_body)
    file_2.close()
    command = ['python', 'workflow' + os.sep + 'static' + os.sep + 'htmldiff.py', 'file_2', 'file_1']
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    text = p.stdout.read()
    os.remove('file_1')
    os.remove('file_2')
    return render(request, 'articles/revision.html', {'revision': revision, 'body': text})

# assignments
@group_required('bronze')
def assignments(request):
    if request.is_ajax():
        if request.GET['action']=='accept':
            asgt = Assignment.objects.get(id=int(request.GET['id']))
            asgt.accepted=True
            asgt.save()
        if request.GET['action']=='finish':
            asgt = Assignment.objects.get(id=int(request.GET['id']))
            asgt.finished=True
            asgt.save()
    assignments = Assignment.objects.all().order_by('accepted','finished')
    type = "all"
    if request.GET.get('progress'):
        type = "progress"
        p = int(request.GET.get('progress'))
        if p == 0:
            assignments = assignments.filter(finished=True)
        else:
            assignments = assignments.filter(finished=False)
    if request.GET.get('type'):
        type = "type"
        assignments = assignments.filter(type=request.GET.get('type'))
    if not Group.objects.get(name='silver') in request.user.groups.all():
        assignments = assignments.filter(receiver=request.user.profile.id)
    return render(request, 'assignment/assignments.html', {'assignments': assignments, 'type': type})

@group_required('bronze')
def filter_by_receiver(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    assignments = Assignment.objects.filter(receiver=profile).order_by('accepted','finished')
    return render(request, 'assignment/assignments.html',
                  {'assignments': assignments, 'type': "receiver"})

@group_required('silver')
def new_assignment(request):
    if request.method == 'GET':
        form = AssignmentForm()
        return render(request, 'assignment/new_assignment.html', {'form': form})
    else:
        form = AssignmentForm(request.POST)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.sender = request.user.profile
            new_assignment.save()
            form.save_m2m
            return redirect(reverse("assignments") + "?progress=1")
        else:
            return render(request, 'assignment/new_assignment.html', {
                'form': form
            })

@group_required('silver')
def edit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == 'GET':
        form = AssignmentForm(instance=assignment)
        return render(request, 'assignment/new_assignment.html', {
            'form': form
        })
    else:
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect(reverse("assignments"))
        return render(request, 'assignment/new_assignment.html', {
            'form': form
        })

@group_required('bronze')
def comment(request,article_id,user_id):
    user = User.objects.get(id=user_id)
    article = Article.objects.get(id=article_id)
    body = request.GET['body']
    comment = Comment(article=article,author=user,body=body)
    comment.save()
    obj = dict()
    obj['author'] = [comment.author.profile.position,comment.author.profile.display_name]
    fmt = '%b. %d, %Y, %I:%M %p'
    obj['created_date'] = comment.created_date.strftime(fmt)
    obj['body'] = comment.body
    return HttpResponse(json.dumps(obj),content_type='application/json')

@group_required('silver')
def copies(request):
    if request.GET.get('delete'):
        id = int(request.GET.get('delete'))
        Copy.objects.get(id=id).delete()
        return redirect(reverse('copies'))
    copies = Copy.objects.order_by('-created_date')
    if request.method=='POST':
        files = request.FILES.getlist('files')
        for file in files:
            copy = Copy(file=file)
            copy.save()
    return render(request,'copies.html',{'copies':copies})

@group_required('silver')
def publish(request,article_id):
    article = Article.objects.get(id=article_id)
    article.published = not article.published
    article.published_date = timezone.now()
    article.save()
    return HttpResponse('success')

