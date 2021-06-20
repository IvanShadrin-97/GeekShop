from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from users.models import User
from admins.forms import AdminUserCreationForm, AdminUserUpdateForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {'title': 'Admin | Users', 'users': User.objects.all()}
#     return render(request, 'admins/admin-user-read.html', context)
#


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-user-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Admin | Users'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#     if request.method == 'POST':
#         form = AdminUserCreationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Новый профиль успешно создан!')
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = AdminUserCreationForm()
#     context = {
#         'title': 'Admin | UserCreate',
#         'form': form
#     }
#     return render(request, 'admins/admin-user-create.html', context)

class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-user-create.html'
    form_class = AdminUserCreationForm
    success_url = reverse_lazy('admins:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = AdminUserUpdateForm(data=request.POST, files=request.FILES, instance=selected_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = AdminUserUpdateForm(instance=selected_user)
#     context = {
#         'title': 'Admin | Update-Delete',
#         'form': form,
#         'selected_user': selected_user,
#         }
#     return render(request, 'admins/admin-user-update-delete.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-user-update-delete.html'
    form_class = AdminUserUpdateForm
    success_url = reverse_lazy('admins:admin_users')



# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):
#     selected_user = User.objects.get(id=id)
#     selected_user.is_active = False
#     selected_user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-user-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    # def delete(self, request, *args, **kwargs):
    #     pass

@user_passes_test(lambda u: u.is_superuser)
def admin_user_recover(request):
    selected_user = User.objects.get(id=id)
    selected_user.is_active = True
    selected_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
