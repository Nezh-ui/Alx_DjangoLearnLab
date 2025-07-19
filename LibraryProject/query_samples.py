import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')

django.setup()
from relationship_app.models import Author, Book, Library, Librarian
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return [f"No author found with that name: {author_name}"]
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return [f"No library found with that name: {library_name}"]
def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return [f"Librarian of {library_name}: {librarian.name}"]
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return [f"No librarian found for library: {library_name}"]