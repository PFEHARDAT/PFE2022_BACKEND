from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from posts.models import Post
from rest_framework import status
from users.models import User
import json

# Create your views here.
class LikesView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        post = Post.objects.get(id=data['post_id'])
        like = Like.objects.filter(user=user, post=post)
        if like.exists():
            like.delete()
            return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(user=user, post=post)
            return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)

class LikedPostView(APIView):   
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        likes = Like.objects.filter(user=user)
        like_list = []
        for like in likes:
            like_list.append(like.post.id)
        return Response({'like_list': like_list}, status=status.HTTP_200_OK)

class LikeOnPostView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        likes = Like.objects.filter(post=post)
        like_list = []
        for like in likes:
            like_list.append(like.user.id)
        return Response({'like_list': like_list}, status=status.HTTP_200_OK)
