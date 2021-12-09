from django.urls import path
from admins.views import IndexListView, UserListView, UserUpdateView, UserCreateView, UserDeleteView, ProductListView, \
    CategoryListView

app_name = 'admins'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('categories/', CategoryListView.as_view(), name='admin_categories'),
]