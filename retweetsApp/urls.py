# /postsApp/urls.py : API urls.py
from django.urls import path
from .views import RetweetAPIView, RetweetListAPIView

urlpatterns = [
    path("create/", RetweetAPIView.as_view(), name="retweet_create"),
    path("delete/<int:user>/<int:post>", RetweetAPIView.as_view(), name="retweet_delete"),
    path("all/<int:user>", RetweetListAPIView.as_view(), name="retweet_all"),
    path("exist/<int:user>/<int:post>", RetweetAPIView.as_view(), name="retweet_exist")
]