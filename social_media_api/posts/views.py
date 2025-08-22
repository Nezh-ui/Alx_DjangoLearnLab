from warnings import filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, filters
from rest_framework import generics
from notifications.models import Notification
from .serializers import CommentSerializer, PostSerializer
from .models import Like, Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType


# Create your views here.
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user

class PostViewset(viewsets.ModelViewSet): # handles post CRUD ops
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewset(viewsets.ModelViewSet): # handles comment CRUD ops
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        if self.request.user != serializer.instance.post.author:
            Notification.objects.create(
                recipient=serializer.instance.post.author,
                actor=self.request.user,
                verb='commented',
                content_type=ContentType.objects.get_for_model(Comment),
                object_id=serializer.instance.id
            )

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated] # handles feed view for posts from followed users

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=pk)  # Get post or return 404
        created = Like.objects.get_or_create(user=request.user, post=post)  # Create like if it doesn't exist
        if created:
            if post.author != request.user:  # Notify post author
                Notification.objects.create(
                    recipient=post.author,
                        actor=request.user,
                        post=post,
                        verb='liked',
                        content_type=ContentType.objects.get_for_model(Like),
                        object_id=post.id
            )
            return Response({"status": "liked"}, status=201)
        return Response({"status": "already liked"}, status=200)

class UnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
            return Response({"status": "unliked"}, status=204)
        except Like.DoesNotExist:
            return Response({"status": "not liked"}, status=400)

   