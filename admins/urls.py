from django.urls import path

from admins.views import index,admin_users, admin_user_create, admin_user_update, admin_user_delete, admin_user_recover


app_name = 'admins'

urlpatterns = [
        path('admin-staf/', index, name='index'),
        path('admin-user/', admin_users, name='admin_users'),
        path('admin_user_create/', admin_user_create, name='admin_user_create'),
        path('admin_user_update/<int:id>/', admin_user_update, name='admin_user_update'),
        path('admin_user_delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
        path('admin_user_recover/<int:id>/', admin_user_recover, name='admin_user_recover'),

]