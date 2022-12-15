from rest_framework import serializers
from .models import Like
from postsApp.serializers import PostSerializerPlus

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post')
    def create(self, validated_data):
        ret = super().create(validated_data)
        ret.save()
        return ret

class LikePostSerializer(PostSerializerPlus):
    super(PostSerializerPlus)