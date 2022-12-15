# /postsApp/urls.py : API urls.py
from django.urls import path
from .views import RetweetAPIView, RetweetListAPIView

urlpatterns = [
    path("", RetweetAPIView.as_view(), name="retweet"),
    path("/all/<int:user>", RetweetListAPIView.as_view(), name="retweet_all"),
]