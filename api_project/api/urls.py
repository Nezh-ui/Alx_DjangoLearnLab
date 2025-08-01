from django.urls import path, include
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# This file is used to define the API URLs for the application.
# It includes the URL for the BookList which lists all books.