# /postsApp/urls.py : API urls.py
from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailsAPIView,
    PostByUserAPIView
)

urlpatterns =[
    path('api', PostListAPIView.as_view()),
    path('api/<int:post_id>', PostDetailsAPIView.as_view())
]