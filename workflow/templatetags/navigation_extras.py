from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def active_nav(request, word):
    if word in request.path:
        return "active"
    return ""