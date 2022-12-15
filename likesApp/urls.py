from django.urls import path
from .views import LikesView, LikedPostView, LikesOnPostView, LikeExistView


urlpatterns = [
    path('', LikesView.as_view()),
    path('/liked_list/<int:user_id>', LikedPostView.as_view()),
    path('/like_list/<int:post_id>', LikesOnPostView.as_view()),
    path("/exist", LikeExistView.as_view(), name="like_exist")
]