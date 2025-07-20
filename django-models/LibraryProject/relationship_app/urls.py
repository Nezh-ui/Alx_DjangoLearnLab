from django.urls import path

from Introduction_to_Django.LibraryProject.bookshelf import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView 
from relationship_app import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:library_name>/books/', LibraryDetailView.as_view(), name='library_books'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.Admin_view, name='admin_view'),
    path('librarian/', views.Librarian_view, name='librarian_view'),
    path('member/', views.Member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit/', views.change_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
# This code defines the URL patterns for the relationship app in a Django project.
# It includes a path for listing all books and a detail view for books in a specific library