from django import template

register = template.Library()


@register.filter
def to_lower(value):
    return value.lower()

