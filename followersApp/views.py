from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics, status
from .serializers import FollowerToUserSerializer
from .models import Follower


# Create your views here.

class AllFollowerView(APIView):
    def get(self, request:Request, user):
        followers = Follower.objects.all().filter(user=user)
        serializer = FollowerToUserSerializer(followers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class FollowerToUserView(APIView):
    serializer_class = FollowerToUserSerializer
    def post(self, request:Request):
        user = request.data.get("user")
        follower = request.data.get("follower")
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Follower Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        follower_exist = Follower.objects.filter(user=user, follower=follower)
        follower_exist.delete()
        return Response(data='DELETED', status=status.HTTP_200_OK)