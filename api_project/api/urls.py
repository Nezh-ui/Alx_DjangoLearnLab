from django.urls import path, include
from api.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
]
# This file is used to define the API URLs for the application.
# It includes the URL for the BookListView which lists all books.