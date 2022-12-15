from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from rest_framework import status
from usersApp.models import User
from postsApp.models import Post
from .serializers import LikeSerializer, LikePostSerializer
from postsApp.views import transformPostData


# Create your views here.
class LikesView(APIView):
    serializer_class = LikeSerializer
    def post(self, request):
        data = {
            'user': request.data.get('user'),
            'post': request.data.get('post')
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            self.updateCount(data['post'], True)
            return Response({'message': 'CREATED', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Like already exists'}, status=status.HTTP_409_CONFLICT)
        
    def delete(self, request):
        user = request.query_params.get('user')
        post = request.query_params.get('post')
        like = Like.objects.filter(user=user, post=post)
        if not like.exists():
            return Response({'message': 'Like does not exist'}, status=status.HTTP_409_CONFLICT)
        like.delete()
        self.updateCount(post, False)
        return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)

    def updateCount(self, post, increment):
        post = Post.objects.get(id=post)
        if increment:
            post.like_count += 1
        else:
            post.like_count -= 1
        post.save()

class LikedPostView(APIView):   
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        likes = Like.objects.filter(user=user)
        posts = Post.objects.filter(id=likes[0].post.id)
        completeData = transformPostData(posts, user_id)
        serializer = LikePostSerializer(completeData, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
