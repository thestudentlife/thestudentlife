from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from mainsite.models import Issue, Section, Article
from workflow.views import ExtraContext
from workflow.views import group_required


@group_required('silver')
def issues(request):
    issues = Issue.objects.order_by('-created_date')
    return render(request,'issues.html',{'issues':issues})

@group_required('silver')
def issue(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    sections = Section.objects.all()
    articles = Article.objects.filter(issue=issue)
    return render(request, 'issue.html', {'issue': issue, 'sections': sections, 'articles': articles, 'permission': request.user.profile.get_highest_group()})

class IssueCreateView(CreateView, ExtraContext):
    model = Issue
    fields = ['name']
    successful_url = reverse_lazy('issues')
    template_name = "create_issue.html"

class IssueEditView(UpdateView, ExtraContext):
    model = Issue
    fields = ['name']
    successful_url = reverse_lazy('issues')
    template_name = "edit_issue.html"