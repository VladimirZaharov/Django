from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop - Админ Панель'
    }
    return render(request, 'admins/index.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
        context = {
            'title': 'GeekShop - Создание пользователей',
            'form': form
        }
        return render(request, 'admins/admin-users-create.html', context)


def admin_users(request):
    context = {
        'title': 'GeekShop - Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-user-read.html', context)


def admin_users_update(request):
    context = {
        'title': 'GeekShop - Обновление пользователя'
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request):
    pass