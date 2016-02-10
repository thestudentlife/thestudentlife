from mainsite.models import Section

def section(request):
    sections = Section.objects.all().order_by('priority')
    return {'sections': sections}