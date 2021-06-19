from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import AdminUserCreationForm, AdminUserUpdateForm


user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {'title': 'Admin | Users', 'users': User.objects.all()}
    return render(request, 'admins/admin-user-read.html', context)


user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новый профиль успешно создан!')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = AdminUserCreationForm()
    context = {
        'title': 'Admin | UserCreate',
        'form': form
    }
    return render(request, 'admins/admin-user-create.html', context)


user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = AdminUserUpdateForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = AdminUserUpdateForm(instance=selected_user)
    context = {
        'title': 'Admin | Update-Delete',
        'form': form,
        'selected_user': selected_user,
        }
    return render(request, 'admins/admin-user-update-delete.html', context)


user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    selected_user = User.objects.get(id=id)
    selected_user.is_active = False
    selected_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


user_passes_test(lambda u: u.is_superuser)
def admin_user_recover(request):
    selected_user = User.objects.get(id=id)
    selected_user.is_active = True
    selected_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
