from django.shortcuts import render
from relationship_app.models import Book
from relationship_app.models import Library  
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def list_books(request):
    books = Book.objects.all()
    if 'library_name' in request.GET:
        library_name = request.GET['library_name']
        books = books.filter(library__name=library_name)
    return render(request, "relationship_app/list_books.html", {"books": books})



from .models import Library, Book 
from django.views.generic.detail import DetailView                              
  
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_queryset(self):
        library_name = self.request.GET.get('library_name', 'Default Library')
        if library_name:
            return Book.objects.filter(library__name=library_name)
        return Book.objects.none()
    
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# This code defines the URL patterns for the relationship app in a Django project.
# It includes a path for listing all books and a detail view for books in a specific library


def is_admin(user):
    return user.is_authenticated and UserProfile.objects.filter(user=user, role='Admin').exists()
def is_librarian(user):
    return user.is_authenticated and UserProfile.objects.filter(user=user, role='Librarian').exists()
def is_member(user):
    return user.is_authenticated and UserProfile.objects.filter(user=user, role='Member').exists()

@user_passes_test(is_admin,)
def Admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
@user_passes_test(is_librarian,)
def Librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
@user_passes_test(is_member,)
def Member_view(request):
    return render(request, 'relationship_app/member_view.html')
