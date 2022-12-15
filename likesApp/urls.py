from django.urls import path
from .views import LikesView, LikedPostView, LikesOnPostView, LikeExistView


urlpatterns = [
    path('', LikesView.as_view()),
    path('/liked_list/<int:user_id>', LikedPostView.as_view())
]