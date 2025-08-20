from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField(source='author.id', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'author_id'] 

    def validate_title(self,value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField(source='author.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_id', 'created_at', 'updated_at']

    def validate_content(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Content must be at least 3 characters long.")
        return value