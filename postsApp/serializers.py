# /postsApp/serializers.py
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["user_id", "content", "publication_date", "like_count", "comment_count", "retweet_count"]