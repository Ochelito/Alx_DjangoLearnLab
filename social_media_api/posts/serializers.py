from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

# Serializer for comments
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # show username

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment content cannot be empty.")
        return value

# Serializer for posts
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # show username
    comments = CommentSerializer(many=True, read_only=True)  # nested comments

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Post title cannot be empty.")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Post content cannot be empty.")
        return value
