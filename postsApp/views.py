from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from usersApp.models import User
from subscriptionsApp.models import Subscription
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
        user_author = User.objects.get(pk=request.data.get('user'))
        data = {
            'user': request.data.get('user'), 
            'content': request.data.get('content'), 
            'publication_date': datetime.datetime.now(),
            'author_pseudo' : getattr(user_author,"username")
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
        post_to_delete = self.get_object(post_id)
        if post_to_delete.response_to_post is not None: # if it's a comment
            main_post = PostDetailsAPIView.get_object(self,post_id=getattr(post_to_delete, "response_to_post_id"))
            main_post.comment_count = main_post.comment_count - 1
            main_post.save() 

        post_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostByUserAPIView(APIView):
    def get(self,request, user_id):
        posts = Post.objects.filter(user = user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class CommentsListAPIView(APIView):
    
    #List all comments of a post
    def get(self, request, post_id):
        comments = Post.objects.filter(response_to_post=post_id)
        serializer = PostSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        # if we try to add a comment to nonexistant post 
        # we throw a 400 
        main_post = PostDetailsAPIView.get_object(self,post_id=post_id) 
        if not main_post:
            return Response(
                {"res": "You tried to comment on a non-existent post!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_author = User.objects.get(pk=request.data.get('user'))

        '''
        Create the post (comment) with given post data
        '''
        data = {
            'user': request.data.get('user'), 
            'content': request.data.get('content'), 
            'publication_date': datetime.datetime.now(),
            'is_comment' : True,
            'response_to_post' : post_id,
            'author_pseudo' : getattr(user_author,"username")
        }

        serializer = PostSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            main_post.comment_count = main_post.comment_count + 1
            main_post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostFromSubscriptionAPIView(APIView):
    def get(self,request,user_id):
        
        subscriptions = Subscription.objects.filter(user=user_id)
        set_sub = {s.subscription.id for s in subscriptions}
        print("#")
        for s in subscriptions:
            print("----",s.subscription,"----")

        print("#")

        # Return all posts created by people, user (id=user_id) is following
        # comments are excluded
        posts = Post.objects.filter(user__in=set_sub).exclude(is_comment=True)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)