from mainsite.models import Section, StaticPage

def section(request):
    sections = Section.objects.all().order_by('priority')
    pages = StaticPage.objects.all()
    return {'sections': sections, 'pages':pages}