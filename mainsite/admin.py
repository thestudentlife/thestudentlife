from django.contrib import admin
from mainsite.models import Photographer,Author,Editor,Section,Issue
# Register your models here.
admin.site.register(Photographer);
admin.site.register(Author);
admin.site.register(Editor);
admin.site.register(Section);
admin.site.register(Issue);