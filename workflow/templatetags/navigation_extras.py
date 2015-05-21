from django import template

register = template.Library()

@register.simple_tag
def active_nav(request, word):
    if word in request.path:
        return "active"
    return ""