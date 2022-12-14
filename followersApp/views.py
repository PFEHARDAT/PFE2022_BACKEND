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

    def post(self, request:Request):
        user = request.data.get("user")
        follower = request.data.get("follower")
        data = request.data
        serializer = self.serializer_class(data=data)
        follower = Follower.objects.filter(user=user, follower=follower)
        if follower.exists():
            follower.delete()
            self.updateFollowerCount(user, False)
            return Response(data='DELETED', status=status.HTTP_200_OK)
        elif serializer.is_valid():
            serializer.save()
            self.updateFollowerCount(user, True)
            response = {"message": "Follower Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    #def delete(self, request:Request):
    #    user = request.data.get("user")
    #    follower = request.data.get("follower")
    #    follower_exist = Follower.objects.filter(user=user, follower=follower)
    #    follower_exist.delete()
    #    self.updateFollowerCount(user, False)
    #    return Response(data='DELETED', status=status.HTTP_200_OK)
    
    def updateFollowerCount(self, user, increment):
        user = User.objects.get(id=user)
        if increment:
            user.followers_count += 1
        else:
            user.followers_count -= 1
        user.save()
