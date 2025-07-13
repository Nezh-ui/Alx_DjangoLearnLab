from bookshelf.models import Book

book = Book.objects.create(
    title="1949",
    author="George Orwell",
    publication_year= "1949"
)
# creates a book instance and assigns values to its variables