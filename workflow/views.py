from django.contrib.auth import authenticate, login as do_login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.context_processors import csrf
from django.forms import inlineformset_factory, ModelForm
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from mainsite.models import Issue, Article, Section, Profile, AssignmentForm, Photo, FrontArticle, CarouselArticle, \
    Album
from workflow.models import Assignment, RegisterForm, LoginForm, WArticle, Revision
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
import os, subprocess
from workflow.static import getText

def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, '/workflow/login')

class ExtraContext():
    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        extra_context = {'permission': self.request.user.profile.get_highest_group()}
        context.update(self.extra_context)
        return context

def register(request):
    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect(reverse('whome'))
        else:
            return render(request, 'register.html', {
                'form': registerForm
            })
    else:
        registerForm = RegisterForm()
        return render(request, 'register.html', {
            'form': registerForm
        })

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

def home(request):
    if request.user.is_anonymous():
        return redirect(reverse('login'))
    elif isMember(request.user, "silver"):
        latest = Issue.objects.latest('created_date')
        return redirect(latest.get_absolute_url())
    else:
        id = request.user.id
        return redirect(reverse('filter_by_receiver', args=[id]))


@group_required('silver')
def front(request):
    if request.method=="GET":
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
        return render(request, 'front.html',{'latest_articles_for_front':latest_articles_for_front,'fronts':fronts,
                                                'latest_articles_for_carousel':latest_articles_for_carousel,
                                                'carousels':carousels})
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
    data = render_to_string('articles/article_xml.xml', {'article': article,'paragraphs':paragraphs})
    return HttpResponse(data, content_type='application/xml')


@group_required('silver')
def revision(request,pk):
    revision = Revision.objects.get(pk=pk);
    article = revision.article;
    index = list(article.revision_set.order_by('date')).index(revision)
    if index > 0:
        previous_revision_body = list(article.revision_set.order_by('date'))[index-1].body
    else:
        previous_revision_body = ''
    file_1 = open('file_1','w')
    file_1.write(revision.body)
    file_1.close()
    file_2 = open('file_2','w')
    file_2.write(previous_revision_body)
    file_2.close()
    command = ['python', 'workflow' + os.sep + 'static' + os.sep + 'htmldiff.py','file_2','file_1']
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    text = p.stdout.read()
    os.remove('file_1')
    os.remove('file_2')
    return render(request, 'articles/revision.html',{'revision':revision,'body':text})


# photos
@group_required('silver')
def photos(request):
    return HttpResponse('These are the photos.')

@group_required('bronze')
def photo(request, photo_id):
    return HttpResponse('This is photo ' + str(photo_id))

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']

@group_required('silver')
def update_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    PhotoInlineFormSet = inlineformset_factory(Album, Photo, form=PhotoForm)
    if request.method == "POST":
        formset = PhotoInlineFormSet(request.POST, request.FILES, instance=album)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.credit = request.user.profile
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            formset.save_m2m()
            return HttpResponse("Success!")
    else:
        formset = PhotoInlineFormSet(instance=album)
    return render_to_response("articles/update_album.html", RequestContext(request, {
        "formset": formset
    }))

@group_required('bronze')
def edit_photo(request, photo_id):
    return HttpResponse('You are going to edit photo ' + str(photo_id))

#assignments
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
    return render(request, 'assignment/assignments.html', {'assignments': assignments, 'permission': request.user.profile.get_highest_group()})

@group_required('bronze')
def filter_by_section(request, section_name):
    section = Section.objects.get(name=section_name)
    assignments = Assignment.objects.filter(section=section)
    return render(request, 'assignment/assignments.html', {'assignments': assignments})

@group_required('bronze')
def filter_by_type(request, type_name):
    assignments = Assignment.objects.filter(type=type_name)
    return render(request, 'assignment/assignments.html', {'assignments': assignments})

def isMember(user, group_name):
    groups = user.groups.all()
    group = Group.objects.get(name=group_name)
    return group in groups
