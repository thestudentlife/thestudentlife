from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from mainsite.models import Issue, Article, Section, Profile, AssignmentForm, FrontArticle, CarouselArticle
from workflow.models import Assignment, RegisterForm, LoginForm, Revision, ProfileForm, RegisterForm2, Comment
import os, subprocess,json
from workflow.static import getText

def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, '/workflow/login')

def register(request):
    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():

            user = registerForm.save(commit=False)
            display_name = user.first_name+" "+user.last_name
            profile = Profile(user=user,display_name=display_name)
            profile.save()
            user.set_password(request.POST['password'])
            user.save()
            plastic = Group.objects.get(name='plastic')
            user.groups.add(plastic)
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
    if request.user.is_anonymous():
        return redirect(reverse('login'))
    elif isMember(request.user, "silver"):
        latest = Issue.objects.latest('created_date')
        return redirect(latest.get_absolute_url())
    else:
        id = request.user.id
        return redirect(reverse('filter_by_receiver', args=[id]))


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
        if form.is_valid():
            user = form.save(commit=False)
        else:
            return render(request,'setting.html',{'form':form})
        second_form = ProfileForm(request.POST,instance=user.profile)
        if second_form.is_valid():
            second_form.save()
        else:
            return render(request,'setting.html',{'form':form})
        user.groups.all().delete()
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

@group_required('silver')
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
    assignments = Assignment.objects.all()
    return render(request, 'assignment/assignments.html', {'assignments': assignments})

@group_required('bronze')
def assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    return render(request, 'assignment/assignment.html', {'assignment': assignment})

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
            return redirect(reverse("assignments"))
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
            assignment = form.save()
            return redirect(reverse("assignments"))
        return render(request, 'assignment/new_assignment.html', {
            'form': form
        })

@group_required('bronze')
def filter_by_receiver(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    assignments = Assignment.objects.filter(receiver=profile)
    return render(request, 'assignment/assignments.html',
                  {'assignments': assignments})

@group_required('bronze')
def filter_by_section(request, section_id):
    section = Section.objects.get(pk=section_id)
    assignments = Assignment.objects.filter(section=section)
    return render(request, 'assignment/assignments.html', {'assignments': assignments})

@group_required('bronze')
def filter_by_type(request, type_name):
    assignments = Assignment.objects.filter(type=type_name)
    return render(request, 'assignment/assignments.html', {'assignments': assignments})

@group_required('bronze')
def comment(request,article_id,user_id):
    user = User.objects.get(id=user_id)
    article = Article.objects.get(id=article_id)
    body = request.GET['body']
    comment = Comment(article=article,author=user,body=body)
    comment.save()
    obj = dict()
    obj['author'] = [comment.author.profile.position,comment.author.profile.display_name]
    fmt = '%Y-%m-%d %H:%M'
    obj['created_date'] = comment.created_date.strftime(fmt)
    obj['body'] = comment.body
    return HttpResponse(json.dumps(obj),content_type='application/json')


@group_required('silver')
def publish(request,article_id):
    article = Article.objects.get(id=article_id)
    article.published = not article.published
    article.published_date = timezone.now()
    article.save()
    return HttpResponse('success')


def isMember(user, group_name):
    groups = user.groups.all()
    group = Group.objects.get(name=group_name)
    return group in groups
