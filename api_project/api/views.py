from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import BookSerializer
from .models import Book
# Create your views here.

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
