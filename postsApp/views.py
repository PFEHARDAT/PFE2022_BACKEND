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

class PostDetailsAPIView(APIView):
    def get_object(self, post_id):
        try:
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, request, post_id):
        post = self.get_object(post_id)

        if not post:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        post = self.get_object(post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
