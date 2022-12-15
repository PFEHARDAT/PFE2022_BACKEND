from rest_framework import serializers
from .models import User, UserFollowed
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def validate(self, attrs):
        email_exist = User.objects.filter(email=attrs["email"]).exists()

        if email_exist:
            raise ValidationError("Email has already been used")
        
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'followers_count', 'following_count')

class UserFollowedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserFollowed
        fields = ('user', 'followed')
        
        
