from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from mainsite.models import Article, Issue,ArticleForm, Album
from workflow.models import WArticle, Revision
from workflow.views import group_required
from django.utils import timezone
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
import subprocess

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/warticle.html"

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'section']
    template_name = 'articles/new_article.html'
    success_url = reverse_lazy('latest_article')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.issue = Issue.objects.get(pk=self.kwargs['issue_id']);
        article.save()
        article.authors.add(self.request.user.profile)
        album = Album(article=article)
        album.save()
        workflowArticle = WArticle(article=article, status='')
        workflowArticle.save()
        return super(ArticleCreateView, self).form_valid(form)

@group_required('silver')
def article_edit(request,issue_id,pk):
    original_article = Article.objects.get(pk=pk)
    original_content = original_article.content
    if request.method == 'GET':
        original_content = original_article.content
        original_second = original_article.updated_date.second
        form = ArticleForm(instance=original_article)
        return render(request,'articles/edit_article.html',
                      {'form':form, 'article': original_article, 'original_content':original_content,'original_second':original_second})
    else:
        base_content = request.POST['original_content']
        base_second = request.POST['original_second']
        form = ArticleForm(request.POST, instance=original_article)
        if form.is_valid():
            if base_second == str(original_article.updated_date.second):
                article = form.save(commit=False)
                article.updated_date = timezone.now()
                article.save()
            else:
                article = form.save(commit=False)
                base = open('base','w')
                me = open('v1','w')
                other = open('v2','w')
                base.write(base_content)
                base.close()
                me.write(article.content)
                me.close()
                other.write(original_content)
                other.close()
                command=['bash','merge.sh']
                p = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
                (output, err) = p.communicate()
                article.content = output
                article.updated_date = timezone.now()
                article.save()
            revision = Revision(article=original_article,
                                    editor=request.user.profile, body=original_article.content)
            revision.save()
            form.save_m2m()
            return redirect(reverse('warticle',args=[issue_id,pk]))
        else:
            return render(request,'articles/edit_article.html',{'form':form, 'article': original_article})



class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_confirm_delete.html"
    success_url = reverse_lazy('whome')

def latest_article(request):
    article = Article.objects.order_by('-updated_date')[0]
    return redirect(reverse('warticle',args=[article.issue.pk,article.pk]))