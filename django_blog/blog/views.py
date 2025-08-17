from tokenize import Comment
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import View
from django.views import generic

from .models import Post
from .forms import CommentForm, CustomUserCreationForm, PostForm
from django.contrib.auth.decorators import login_required
from .forms import CustomProfileUpdateForm, CustomUserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment


# Create your views here.
def register(request): # User registration view
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User registered successfully!")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request): # Profile view for logged-in users
    user_form = CustomUserUpdateForm(instance=request.user)
    profile_form = CustomProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        profile_form = CustomProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponse("Profile updated successfully!")
        else:
            return HttpResponse("Error updating profile.")

    return render(request, 'registration/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(generic.CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentCreateView(generic.CreateView, LoginRequiredMixin): # Comment create view
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form): # Comment form validation
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

   

class CommentUpdateView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin): # Comment update view
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin): 
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):  
        comment = self.get_object()
        return self.request.user == comment.author # Check if the logged-in user is the author of the comment
