from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from relationship_app.models import Book, Library   
def list_books(request):
    books = Book.objects.all()
    list_books = [f"{book.title} by {book.author}" for book in books]
    return render(request, "relationship_app/list_books.html", {"books": books})


from query_samples import List_all_books_in_library
from django.views.generic import ListView                                
from bookshelf.models import Book
from relationship_app.models import Library 

class LibraryBooksView(ListView):
    model = Book
    template_name = 'list_books.html'

    def get_queryset(self):
        library_name = self.request.GET.get('library_name', 'Default Library')
        if library_name:
            return Book.objects.filter(library__name=library_name)
        return Book.objects.none()
    
