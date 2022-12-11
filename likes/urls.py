from django.urls import path
from . import views
from .views import LikesView

urlsPatterns = [
    path('like/', LikesView.as_view()),
    path('liked_list/<int:user_id>', LikesView.as_view()),
    path('like_list/<int:post_id>', LikesView.as_view())
]