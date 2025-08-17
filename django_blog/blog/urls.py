from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', views.register, name='register'), # User registration view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # Login view for users
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'), # Logout view for logged-in users
    path('profile/', views.profile, name='profile'), # Profile view for logged-in users
    path('post/', PostListView.as_view(), name='post-list'), # List view for all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # Detail view for a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'), # Create view for new posts
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update view for existing posts
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete view for existing posts
    path('post/<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='comment-create'), # Create view for new comments
    path('post/<int:pk>/comment/<int:comment_pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'), # Update view for existing comments
    path('post/<int:pk>/comment/<int:comment_pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'), # Delete view for existing comments
]