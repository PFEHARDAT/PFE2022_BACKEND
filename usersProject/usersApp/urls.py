from django.urls import path
from .views import UserListAPIView


urlpatterns = [
    path('api', UserListAPIView.as_view()),
]