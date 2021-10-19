from products.models import Product, ProductCategory

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'geekshop - каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
               }
    return render(request, 'products/products.html', context)
