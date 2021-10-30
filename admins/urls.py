from django.urls import path
from admins.views import IndexListView, UserListView, UserUpdateView, UserCreateView, UserDeleteView

app_name = 'baskets'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove')
]