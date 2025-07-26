from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Author
from .models import UserProfile

# Create your views here.
UserProfile.objects.filter(user__username='desired_username')

@permission_required('bookshelf.can_view_author')
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'bookshelf/author_list.html', {'authors': authors})

@permission_required('bookshelf.can_create_author')
def create_author(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/create_author.html')

@permission_required('bookshelf.can_edit_author')
def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/edit_author.html', {'author': author})

@permission_required('bookshelf.can_delete_author')
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'bookshelf/delete_author.html', {'author': author})