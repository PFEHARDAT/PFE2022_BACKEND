from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Retweet
from .models import Post 
from .serializers import RetweetSerializer, RetweetPostSerializer


import datetime

# Create your views here.


class RetweetAPIView(APIView):
    serializer_class = RetweetSerializer
    def post(self, request:Request):
        user = request.data.get("user")
        post = request.data.get("post")
        data = {
            'user': user,
            'post' : post,
            'retweet_date' : datetime.datetime.now()
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            main_post = Post.objects.get(id=post)
            main_post.retweet_count += 1
            main_post.save()
            response = {"message": "Retweet Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self , request:Request):
        user = request.data.get("user")
        post = request.data.get("post")
        retweet_exist = Retweet.objects.filter(user=user, post=post)
        main_post = Post.objects.get(id=post)
        main_post.retweet_count -= 1
        main_post.save()
        retweet_exist.delete()
        return Response(data='DELETED', status=status.HTTP_200_OK)

    def get(self, request:Request, user):
        retweets = Retweet.objects.all().filter(user=user)
        serializer = RetweetPostSerializer(retweets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


