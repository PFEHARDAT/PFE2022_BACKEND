# /postsApp/urls.py : API urls.py
from django.urls import path
from .views import RetweetAPIView

urlpatterns =[
    path("create/", RetweetAPIView.as_view(), name="retweet_create"),
    path("delete/", RetweetAPIView.as_view(), name="retweet_delete"),
    path("all/<int:user>", RetweetAPIView.as_view(), name="retweet_all")
]