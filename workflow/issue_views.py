from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from mainsite.models import Issue, Section, Article
from workflow.views import group_required

@group_required('silver')
def issues(request):
    issues = Issue.objects.order_by('-created_date')
    return render(request, 'articles/issues/issues.html', {'issues': issues})

@group_required('silver')
def issue(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    sections = Section.objects.all()
    articles = Article.objects.filter(issue=issue)
    return render(request, 'articles/issues/issue.html', {'issue': issue, 'sections': sections, 'articles': articles})

@group_required('silver')
def latest_issue(request):
    latest = Issue.objects.latest('created_date')
    return issue(request, latest.pk)

class IssueCreateView(CreateView):
    model = Issue
    fields = ['name']
    successful_url = reverse_lazy('issues')
    template_name = "articles/issues/create_issue.html"

class IssueEditView(UpdateView):
    model = Issue
    fields = ['name']
    successful_url = reverse_lazy('issues')
    template_name = "articles/issues/edit_issue.html"

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = "articles/issues/issue_confirm_delete.html"
    success_url = reverse_lazy('issues')