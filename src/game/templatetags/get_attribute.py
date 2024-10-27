from django import template

register = template.Library()


@register.filter(name='getattr')
def get_attribute(value, arg):
    obj = value
    attr = arg
    return getattr(obj, attr, None)
