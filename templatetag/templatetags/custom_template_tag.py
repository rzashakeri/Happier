from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime

register = template.Library()


@register.filter
def minus(value):
    return value - 1


@register.filter
def time_format(value):
    received_time = naturaltime(value).split(",")[0]
    print(received_time)
    if "year" in received_time:
        return value.strftime("%d %b %Y")
    elif "month" in received_time:
        return value.strftime("%d %b %Y")
    elif "week" in received_time:
        return value.strftime("%d %b %Y")
    elif "day" in received_time:
        return value.strftime("%d %b %Y")
    else:
        return received_time
