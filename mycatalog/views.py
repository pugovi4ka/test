from django.http import HttpResponse
from django.shortcuts import  render
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


