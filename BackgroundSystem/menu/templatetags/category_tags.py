# coding:utf-8
from django import template
from menu.models import Menu

register = template.Library()

@register.inclusion_tag("menu/includes/category_tree_part.html")
def category_tree(cate):
        return {'categories':cate.children.all()}


