import json
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from mycatalog.forms import ProductEditForm
from mycatalog.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def catalog(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'mycatalog/catalog.html', {'products': products})


def product_page(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'mycatalog/product_page.html', {'product': product})


def is_superuser_check(user):
    return user.is_superuser


@user_passes_test(is_superuser_check, '/admin/')
def edit(request, id):
    product = Product.objects.get(pk=id)
    form = ProductEditForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponse(json.dumps({
            'message': 'Product saved',
            'form': render_to_string('mycatalog/edit_product_form.html', {'form': form})
        }), content_type='application/json')
    else:
        if request.POST:
            return render(request, 'mycatalog/edit_product_form.html', {'form': form})
        else:
            return render(request, 'mycatalog/edit_product.html', {'product': product, 'form': form})




