from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewset, CommentViewset

router = DefaultRouter()
router.register(r'posts', PostViewset)
router.register(r'comments', CommentViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]