from django.shortcuts import render

from .models import UserProfile

# Create your views here.
UserProfile.objects.filter(user__username='desired_username')
