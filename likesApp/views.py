from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from rest_framework import status
from usersApp.models import User
from postsApp.models import Post

# Create your views here.
class LikesView(APIView):
    def post(self, request):
        data = {
            'user_id': request.data.get('user_id'),
            'post_id': request.data.get('post_id')
        }
        user = User.objects.get(id=data['user_id'])
        post = Post.objects.get(id=data['post_id'])
        like = Like.objects.filter(user=user, post=post)
        if like.exists():
            like.delete()
            self.updateCount(post, False)
            return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(user=user, post=post)
            self.updateCount(post, True)
            return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)

    def updateCount(self, post, increment):
        print("hey")
        if increment:
            post.like_count += 1
        else:
            post.like_count -= 1
        post.save()
class LikedPostView(APIView):   
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        likes = Like.objects.filter(user=user)
        like_list = []
        for like in likes:
            like_list.append(like.post.id)
        return Response({'like_list': like_list}, status=status.HTTP_200_OK)

class LikesOnPostView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        likes = Like.objects.filter(post=post)
        like_list = []
        for like in likes:
            like_list.append(like.user.id)
        return Response({'like_list': like_list}, status=status.HTTP_200_OK)
