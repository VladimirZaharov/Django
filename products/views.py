import os
import json

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)
# Create your views here.
def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'products/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'geekshop - каталог',
        'products': json.dump(products.Product),
        'categories': json.dump(products.ProductCategories)
               }
    return render(request, 'products/products.html', context)
