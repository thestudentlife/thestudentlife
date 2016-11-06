from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from mainsite.models import StaticPage
from workflow.views import group_required

@group_required('silver')
def pages(request):
    pages = StaticPage.objects.all()
    return render(request, 'pages/pages.html', {'pages': pages})

class PageCreateView(CreateView):
    model = StaticPage
    fields = ['name', 'title', 'content']
    template_name = "pages/create_page.html"

class PageEditView(UpdateView):
    model = StaticPage
    fields = ['name', 'title', 'content']
    template_name = "pages/edit_page.html"

class PageDeleteView(DeleteView):
    model = StaticPage
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy('pages')