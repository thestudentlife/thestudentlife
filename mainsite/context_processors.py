from mainsite.models import Section, StaticPage
from website.settings import GOOGLE_SEARCH_CX
def section(request):
    sections = Section.objects.all().order_by('priority')
    pages = StaticPage.objects.all()
    return {'sections': sections, 'pages': pages, 'cx': GOOGLE_SEARCH_CX}