from django.urls import path
from users.views import LoginLoginView,registration,ProfileUpdateView, LogoutLogoutView, verify

app_name = 'users'

urlpatterns = [
    path('login/',LoginLoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<str:activation_key>', verify, name='verify'),
]
