from django.urls import path
from . import views




urlpatterns = [
    path("all/<int:user>", views.FollowerView.as_view(), name="follower_all"),
    path("create/", views.FollowerView.as_view(), name="follower_create"),
    path("delete/", views.FollowerView.as_view(), name="follower_delete")
]