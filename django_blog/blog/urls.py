from django.contrib import admin
from django.urls import include, path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'), # User registration view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # Login view for users
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'), # Logout view for logged-in users
    path('profile/', views.profile, name='profile') # Profile view for logged-in users
]