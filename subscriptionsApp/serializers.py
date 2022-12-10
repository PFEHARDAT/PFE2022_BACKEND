from rest_framework import serializers
from .models import Subscription
from .models import User
from rest_framework.validators import ValidationError

class AllSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.ForeignKey(User)
    subscription = serializers.ForeignKey(User)
    class Meta:
        model = Subscription
        fields= ('id', 'user', 'subscription')
    
    def get_all_subscription(self, attrs):
        subscriptions = Subscription.objects.all().filter(user=attrs["user"])

        return subscriptions

class SubscribeToUserSerializer(serializers.ModelSerializer):
    user = serializers.ForeignKey(User)
    subscription = serializers.ForeignKey(User)

    class Meta:
        model = Subscription
        fields= ('id', 'user', 'subscription')

    def validate(sellf, attrs):
        subscription_exist = Subscription.objects.filter(user=attrs["user"], subscription=attrs["subscription"]).exists()
        if subscription_exist:
            raise ValidationError("Subscription has already been used")
        return super().validate(attrs)

    def create(self, validated_data):
        subscritpion = super().create(validated_data)
        subscritpion.save()
        return subscritpion


