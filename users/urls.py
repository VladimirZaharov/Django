from django.urls import path
from users.views import LoginLoginView,RegistrationCreateView,ProfileUpdateView, LogoutLogoutView

app_name = 'users'

urlpatterns = [
    path('login/',LoginLoginView.as_view(), name='login'),
    path('registration/', RegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
]
