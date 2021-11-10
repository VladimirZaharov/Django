from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket
from users.models import User
# Create your views here.


class LoginLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm


    def get_context_data(self, **kwargs):
        context = super(LoginLoginView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Авторизация'
        return context

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'GeekShop - Авторизация',
#         'form': form
#     }
#     return render(request, 'users/login.html', context)


# class RegistrationCreateView(CreateView):
#     model = User
#     template_name = 'users/registration.html'
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('users:login')
#
#     def get_context_data(self, **kwargs):
#         context = super(RegistrationCreateView, self).get_context_data(**kwargs)
#         context['title'] = 'GeekShop - Регистрация'
#         return context

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Сообщение пользователю отправлено.')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, 'Сообщение пользователю НЕ отправлено.')
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


class ProfileUpdateView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Профиль'
        # context['baskets'] = Basket.objects.filter(user=)  # так и не понял что сюда передать
        return context

# @login_required
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=user)
#     context = {
#         'title': 'GeekShop - Профиль',
#         'form': form,
#         'baskets': Basket.objects.filter(user=user)
#     }
#     return render(request, 'users/profile.html', context)
#


class LogoutLogoutView(LogoutView):
    next_page = 'index'

#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'users/verify.html')
        else:
            messages.error(request, f'error activation user: {user}')
            return render(request, 'users/verify.html')
    except Exception as err:
        messages.error(request, f'error activation user: {user}')
        return HttpResponseRedirect(reverse('index'))


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])

    title = f'Подтвердите учетную запись {user.username}'

    message = f'Для подтверждения учетной записи {user.username} ' \
              f'на портале {settings.DOMAIN_NAME} перейдите по ссылке: \n' \
              f'{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)