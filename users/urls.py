from django.urls import path
from users.views import LoginLoginView,registration,profile, LogoutLogoutView, verify

app_name = 'users'

urlpatterns = [
    path('login/',LoginLoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<str:activation_key>', verify, name='verify'),
]
