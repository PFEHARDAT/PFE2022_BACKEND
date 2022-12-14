from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from rest_framework import status
from usersApp.models import User
from postsApp.models import Post
from .serializers import LikePostSerializer, LikeUserSerializer, LikeSerializer

# Create your views here.
class LikesView(APIView):
    serializer_class = LikeSerializer
    def post(self, request):
        data = {
            'user': request.data.get('user'),
            'post': request.data.get('post')
        }
        like = Like.objects.filter(user=data['user'], post=data['post'])
        serializer = self.serializer_class(data=data)
        print(serializer.is_valid())
        if like.exists():
            like.delete()
            self.updateCount(data['post'], False)
            return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
        elif serializer.is_valid():
            serializer.save()
            self.updateCount(data['post'], True)
            return Response({'message': 'CREATED', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
        return Response({'message': 'Like already exists'}, status=status.HTTP_409_CONFLICT)

    def get(self, request):
        user = request.data.get("user")
        post = request.data.get("post")
        if Like.objects.filter(user=user, post=post).exists():
            return Response(data= "True", status=status.HTTP_200_OK)
        return Response(data= "False", status=status.HTTP_200_OK)
        
    #def delete(self, request):
    #    data = {
    #        'user': request.data.get('user'),
    #        'post': request.data.get('post')
    #    }
    #    like = Like.objects.filter(user=data['user'], post=data['post'])
    #    if not like.exists():
    #        return Response({'message': 'Like does not exist'}, status=status.HTTP_409_CONFLICT)
    #    like.delete()
    #    self.updateCount(data['post'], False)
    #    return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
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
        like_list = []
        for like in likes:
            like_list.append(like)
        serializer = LikePostSerializer(likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class LikesOnPostView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        likes = Like.objects.filter(post=post)
        like_list = []
        for like in likes:
            like_list.append(like)
        serializer = LikeUserSerializer(likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class CSRFTokenView(APIView):
    def get(self, request):
        return Response(data={'csrfToken': request.META['CSRF_COOKIE']}, status=status.HTTP_200_OK)
