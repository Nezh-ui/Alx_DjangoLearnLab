from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .models import UserProfile

# Create your views here.
UserProfile.objects.filter(user__username='desired_username')

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})