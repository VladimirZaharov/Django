from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import products, products_ajax

app_name = 'products'

urlpatterns = [
    path('',products, name='index'),
    path('ajax/',cache_page(3600)(products_ajax)),
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>', products, name='page')
]