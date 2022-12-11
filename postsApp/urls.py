# /postsApp/urls.py : API urls.py
from django.urls import path
from .views import (
    PostListAPIView
)

urlpatterns =[
    path('api', PostListAPIView.as_view())
]