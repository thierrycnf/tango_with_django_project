from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(context, category=None):
    categories = Category.objects.all()
    return {'categories': Category.objects.all(),
            'current_category': category}