from rest_framework import serializers
from .models import Like
from postsApp.serializers import PostSerializer
from usersApp.serializers import UserSerializer


class LikePostSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at')

class LikeUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Like
        fields = ('id', 'post', 'user', 'created_at')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post')
    def create(self, validated_data):
        ret = super().create(validated_data)
        ret.save()
        return ret