from django import template

register = template.Library()

@register.filter
def in_grups(user, group_name):
    return user.groups.filter(name=group_name.strip()).exists()