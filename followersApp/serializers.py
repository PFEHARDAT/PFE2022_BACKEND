from .models import Follower
from .models import User
from rest_framework import serializers
    
   

class FollowerToUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Follower
        fields= ('id', 'user', 'follower')

    def create(self, validated_data):
        fol = super().create(validated_data)
        fol.save()
        return fol