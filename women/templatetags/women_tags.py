from django import template
from women.models import *

register = template.Library()


@register.inclusion_tag('women/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('women/tags/nav_bar.html')
def nav_bar():
    return