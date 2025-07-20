from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView 
from .views import RegisterView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:library_name>/books/', LibraryDetailView.as_view(), name='library_books'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
]
# This code defines the URL patterns for the relationship app in a Django project.
# It includes a path for listing all books and a detail view for books in a specific library