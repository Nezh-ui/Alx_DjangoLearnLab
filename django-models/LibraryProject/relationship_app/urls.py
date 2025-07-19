from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:library_name>/books/', LibraryDetailView.as_view(), name='library_books'),
]
# This code defines the URL patterns for the relationship app in a Django project.
# It includes a path for listing all books and a detail view for books in a specific library