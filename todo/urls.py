from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, delete_task, toggle_task, register

urlpatterns = [
    path('', index, name='home'),
    path('delete/<int:id>/', delete_task, name='delete'),
    path('toggle/<int:id>/', toggle_task, name='toggle'),

     # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),

]
