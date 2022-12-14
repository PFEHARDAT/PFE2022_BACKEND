from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics, status
from .serializers import FollowerToUserSerializer
from .models import Follower
from usersApp.models import User


# Create your views here.

class FollowerView(APIView):
    serializer_class = FollowerToUserSerializer
    def get(self, request:Request, user):
        followers = Follower.objects.all().filter(user=user)
        serializer = FollowerToUserSerializer(followers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)