from django.urls import path

from admins.views import index,UserListView, UserCreateView, UserUpdateView, UserDeleteView, admin_user_recover


app_name = 'admins'

urlpatterns = [
        path('admin-staf/', index, name='index'),
        path('admin-user/', UserListView.as_view(), name='admin_users'),
        path('admin_user_create/', UserCreateView.as_view(), name='admin_user_create'),
        path('admin_user_update/<int:pk>/', UserUpdateView.as_view(), name='admin_user_update'),
        path('admin_user_delete/<int:pk>/', UserDeleteView.as_view(), name='admin_user_delete'),
        path('admin_user_recover/<int:id>/', admin_user_recover, name='admin_user_recover'),

]