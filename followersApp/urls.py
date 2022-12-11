from django.urls import path
from . import views




urlpatterns = [
    path("all/<int:user>", views.AllFollowerView.as_view(), name="follower_all"),
    path("create/", views.FollowerToUserView.as_view(), name="follower_create")
]