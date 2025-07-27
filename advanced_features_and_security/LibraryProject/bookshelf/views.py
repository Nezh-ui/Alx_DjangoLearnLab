from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .models import UserProfile
from .forms import ExampleForm

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


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., save to the database)
            return redirect('success_page')  # Change this to your actual success page
    else:
        form = ExampleForm()
    
    return render(request, 'form_template.html', {'form': form})


