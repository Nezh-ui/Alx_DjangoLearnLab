from django.urls import path
from .views import list_books, LibraryBooksView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:library_name>/books/', LibraryBooksView.as_view(), name='library_books'),
]
