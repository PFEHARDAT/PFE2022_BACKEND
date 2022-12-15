# /postsApp/serializers.py
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "content",
            "publication_date",
            "like_count", 
            "comment_count", 
            "retweet_count",
            "is_comment",
            "response_to_post",
            "author_pseudo"
            ]

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "user",
            "content"
            ]