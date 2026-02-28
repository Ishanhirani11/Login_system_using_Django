from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('create/', views.create_task, name='create'),
    path('update/<int:pk>/', views.update_task, name='update'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle'),
    path('view/<int:pk>/', views.view_task, name='view'),
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='change_password.html',success_url='/profile/'),
    name='change_password'),

]

