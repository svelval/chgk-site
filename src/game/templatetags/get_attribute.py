from django import template

register = template.Library()


@register.filter(name='getattr')
def get_attribute(value, arg):
    obj = value
    attr = arg
    return getattr(obj, attr, None)


@register.simple_tag(name='get_absolute_url')
def get_absolute_url(value):
    return getattr(value, 'get_absolute_url', str)()
