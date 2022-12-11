from .models import Subscription
from .models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError
    
   

class SubscribeToUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Subscription
        fields= ('id', 'user', 'subscription')

    def create(self, validated_data):
        sub = super().create(validated_data)
        sub.save()
        return sub


