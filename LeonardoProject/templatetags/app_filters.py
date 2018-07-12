from django import template

register = template.Library()


@register.filter
def listIndex(List, i):
    return List[int(i)]