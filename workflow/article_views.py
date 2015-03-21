from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from mainsite.models import Article
from workflow.models import WArticle, Revision
from workflow.views import ExtraContext

class ArticleDetailView(DetailView, ExtraContext):
    model = Article
    template_name = "articles/warticle.html"

class ArticleCreateView(CreateView, ExtraContext):
    model = Article
    fields = ['title', 'content', 'section', 'issue', 'authors']
    template_name = 'articles/new_article.html'
    success_url = reverse_lazy('whome')

    def form_valid(self, form):
        obj = form.save()
        obj.save()
        workflowArticle = WArticle(article=obj, status='')
        workflowArticle.save()
        return super(ArticleCreateView, self).form_valid(form)

class ArticleEditView(UpdateView, ExtraContext):
    model = Article
    fields = ['title', 'content', 'section', 'issue', 'authors']
    template_name = 'articles/edit_article.html'
    success_url = reverse_lazy('whome')

    def form_valid(self, form):
        obj = form.save()
        obj.save()
        body = obj.content
        editor = self.request.user.profile
        revision = Revision(article=obj, editor=editor, body=body)
        revision.save()
        return super(ArticleEditView, self).form_valid(form)

class ArticleDeleteView(DeleteView, ExtraContext):
    model = Article
    template_name = "articles/article_confirm_delete.html"
    success_url = reverse_lazy('whome')