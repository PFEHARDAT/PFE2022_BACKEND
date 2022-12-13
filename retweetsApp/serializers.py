from rest_framework import serializers
from .models import Retweet
from .models import Post 
from postsApp.serializers import PostSerializer



class RetweetPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Retweet
        fields = ('id', 'user', 'post', 'retweet_date')

class RetweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retweet
        fields = ('id', 'user', 'post', 'retweet_date')
    

    def create(self, validated_data):
        ret = super().create(validated_data)
        ret.save()
        return ret
