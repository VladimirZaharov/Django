from django.template.loader import render_to_string

from products.models import Product, ProductCategory

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
from django.http import JsonResponse



# Create your views here.
@cache_page(3600)
def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)

def products_ajax(request, category_id=None, page=1):
    if request.is_ajax():
        context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()
        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context['products'] = products_paginator
        result = render_to_string('products/inc_header.html', context=context, request=request)
    return JsonResponse({'result': result})
