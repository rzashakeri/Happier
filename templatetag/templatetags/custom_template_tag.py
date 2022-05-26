from django import template

register = template.Library()


@register.filter
def minus(value):
    return value - 1
