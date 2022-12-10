from .models import Subscription
from .models import User
from rest_framework import serializers
from usersApp.serializers import SignUpSerializer

from rest_framework.validators import ValidationError
    
   

class SubscribeToUserSerializer(serializers.ModelSerializer):
    user=SignUpSerializer(read_only=True, many=True)
    subscription=SignUpSerializer(read_only=True, many=True)
    class Meta:
        model = Subscription
        fields= ('id', 'user', 'subscription')

    def validate(sellf, attrs):
        subscription_exist = Subscription.objects.filter(user=attrs["user"], subscription=attrs["subscription"]).exists()
        if subscription_exist:
            raise ValidationError("Subscription has already been used")
        return super().validate(attrs)

    def create(self, validated_data):
        sub = super().create(validated_data)
        sub.save()
        return sub


