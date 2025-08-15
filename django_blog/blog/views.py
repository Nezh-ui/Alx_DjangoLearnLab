from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomProfileUpdateForm, CustomUserUpdateForm


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
