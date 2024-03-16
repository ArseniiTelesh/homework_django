from django import template

register = template.Library()


@register.simple_tag()
def images_tag(val):
    if val:
        return f'/media/{val}'

    return '#'
