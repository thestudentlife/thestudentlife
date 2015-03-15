from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from django.template.loader import render_to_string
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from mainsite.models import Issue, Article, Section, Profile
from workflow.models import Assignment, RegisterForm, LoginForm

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
            registerForm.save()
            return HttpResponse('Thanks for registering')
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
            do_login(request,user)
            next = request.GET.get('next')
            if next is None:
                return HttpResponse('Welcome')
            else:
                return HttpResponseRedirect(request.GET['next'])
        else:
            return render(request,'login.html',{
            'form':loginForm
            })
    else:
        loginForm = LoginForm()
        return render(request,'login.html',{
            'form': loginForm
        })

def home(request):
    issue = Issue.objects.all()[:1].get()
    return HttpResponse('This should be the latest issue.')

# issues
@group_required('silver')
def issues(request):
    issues = Issue.objects.all()
    return HttpResponse('These are the issues.')

@group_required('silver')
def issue(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    sections = Section.objects.all()
    articles = Article.objects.filter(issue=issue)
    return render(request,'issue.html',{'issue':issue,'sections':sections,'articles':articles})

@group_required('silver')
def new_issue(request):
    return HttpResponse('Create a new issue')


#articles
def article_by_author(request,author_id):
    author = Profile.objects.get(id=author_id)
    articles = Article.objects.filter(author=author)

@group_required('silver')
def article(request, issue_id, article_id, article_name="default"):
    return HttpResponse('This is issue ' + str(issue_id) + " and article " + str(article_id) + ' with name ' + article_name)

@login_required(login_url='/workflow/login/')
def new_article(request, issue_id):
    return HttpResponse('Create a new article in issue ' + str(issue_id))

@group_required('silver')
def edit_article(request, issue_id, article_id, article_name="default"):
    return HttpResponse('You are going to edit article ' + str(article_id) + ' with name ' + article_name)

@group_required('silver')
def delete_article(request, issue_id, article_id, article_name="default"):
    return HttpResponse('You are going to delete article ' + str(article_id) + ' with name ' + article_name)

@group_required('silver')
def article_xml(request,article_id):
    article = Article.objects.get(id=article_id)
    data = render_to_string('article_xml.xml',{'article':article})
    return HttpResponse(data,content_type='application/xml')

#photos
@group_required('silver')
def photos(request):
    return HttpResponse('These are the photos.')

@group_required('bronze')
def photo(request, photo_id):
    return HttpResponse('This is photo ' + str(photo_id))

@group_required('bronze')
def new_photo(request):
    return HttpResponse('Create a new photo')

@group_required('bronze')
def edit_photo(request, photo_id):
    return HttpResponse('You are going to edit photo ' + str(photo_id))

#assignments
@group_required('bronze')
def assignments(request):
    assignments = Assignment.objects.all()
    return render(request,'assignments.html',{'assignments':assignments})

@group_required('bronze')
def assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    return render(request,'assignment.html',{'assignment':assignment})

@group_required('silver')
def new_assignment(request):
    return HttpResponse('Create a new assignment')

@group_required('silver')
def edit_assignment(request, assignment_id):
    return HttpResponse('You are going to edit assignment ' + str(assignment_id))

@group_required('bronze')
def filter_by_receiver(request, profile_id):
    return HttpResponse('The assignments of the profile ' + str(profile_id))

@group_required('bronze')
def filter_by_section(request, section_name):
    return HttpResponse('The assignments of the section ' + str(section_name))

@group_required('bronze')
def filter_by_type(request, type_name):
    return HttpResponse('The assignments of the type ' + str(type_name))

