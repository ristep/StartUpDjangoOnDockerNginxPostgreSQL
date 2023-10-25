from django import template

register = template.Library()


@register.filter
def my_filter(value):
    # your code here
    pass


@register.filter
def hash(h, key):
    return h[key]


@register.filter
def get(dictionary, key):
    return dictionary.get(key)
