from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView, LikeView, PostViewset, CommentViewset, UnlikeView

router = DefaultRouter()
router.register(r'posts', PostViewset)
router.register(r'comments', CommentViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('like/<int:pk>/', LikeView.as_view(), name='like-post'),
    path('unlike/<int:pk>/', UnlikeView.as_view(), name='unlike-post'),

]