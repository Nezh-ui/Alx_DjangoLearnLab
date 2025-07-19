from django.shortcuts import render

# Create your views here.
from query_samples import List_all_books_in_library
def list_books(request):
    library_name = request.GET.get('library_name', 'Default Library')
    books = List_all_books_in_library(library_name)
    return render(request, 'books_list.html', {"books": books})

from query_samples import List_all_books_in_library
from django.views.generic import ListView
from bookshelf.models import Book
class LibraryBooksView(ListView):
    model = Book
    template_name = 'books_list.html'

    def get_queryset(self):
        library_name = self.request.GET.get('library_name', 'Default Library')
        if library_name:
            return Book.objects.filter(library__name=library_name)
        return Book.objects.none()
    
    