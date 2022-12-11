from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
import datetime
# Create your views here.

class PostListAPIView(APIView):

    #List all Post
    def get(self,request):
        '''
        List all the post items
        '''
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    #Create one Post
    def post(self, request):
        '''
        Create the post with given post data
        '''
        data = {
            'user': request.data.get('user'), 
            'content': request.data.get('content'), 
            'publication_date': datetime.datetime.now(),
            'like_count' : 0,
            'comment_count' : 0,
            'retweet_count' : 0
        }

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
