# /postsApp/urls.py : API urls.py
from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailsAPIView,
    PostByUserAPIView,
    CommentsListAPIView,
    PostFromSubscriptionAPIView
)

urlpatterns =[
    path('', PostListAPIView.as_view()),
    path('<int:post_id>', PostDetailsAPIView.as_view()),
    path('user/<int:user_id>', PostByUserAPIView.as_view()),
    path('comments', CommentsListAPIView.as_view()),
    path('comments/<int:post_id>', CommentsListAPIView.as_view()),
    path('subscription/<int:user_id>', PostFromSubscriptionAPIView.as_view())
]