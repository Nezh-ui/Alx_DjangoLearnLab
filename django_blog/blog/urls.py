from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from.views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', views.register, name='register'), # User registration view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # Login view for users
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'), # Logout view for logged-in users
    path('profile/', views.profile, name='profile'), # Profile view for logged-in users
    path('posts/', PostListView.as_view(), name='post-list'), # List view for all posts
    path('posts/create/', PostCreateView.as_view(), name='post-create'), # Create view for new posts
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update view for existing posts
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete view for existing posts
]