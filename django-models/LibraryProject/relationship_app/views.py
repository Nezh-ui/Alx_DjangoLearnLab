from django.shortcuts import render
from relationship_app.models import Book
from relationship_app.models import Library

def list_books(request):
    books = Book.objects.all()
    list_books = [f"{book.title} by {book.author}" for book in books]
    return render(request, "relationship_app/list_books.html", {"books": books})


from django.views.generic import DetailView 
from .models import Library, Book                               
  
class LibraryBooksView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_queryset(self):
        library_name = self.request.GET.get('library_name', 'Default Library')
        if library_name:
            return Book.objects.filter(library__name=library_name)
        return Book.objects.none()
    
