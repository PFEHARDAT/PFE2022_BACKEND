from django.urls import path
from .views import (
    UserListAPIView,
    UserDetailAPIView
    )


urlpatterns = [
    path('api', UserListAPIView.as_view()),
    path('api/<int:pk>', UserDetailAPIView.as_view())
]