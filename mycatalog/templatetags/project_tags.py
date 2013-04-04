from django import template
from mycatalog import Product


register = template.Library()

@register.inclusion_tag('mycatalog/tags/product_list.html', takes_context=True)
def product_list(context):

    product_list = Product.objects.all().order_by('?')

    return {
        'product_list': product_list,
    }


