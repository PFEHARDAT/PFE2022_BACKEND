from django.urls import path
from .views import (
    UserListAPIView,
    UserDetailAPIView,
    UpdateFollowersCountView,
    UpdateFollowingCountView,
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views



urlpatterns = [
    path('/', UserListAPIView.as_view()),
    path('/<int:pk>', UserDetailAPIView.as_view()),
    path('followers/<int:pk>&<bool:increment>', UpdateFollowersCountView.as_view()),
    path('following/<int:pk>&<bool:increment>', UpdateFollowingCountView.as_view()),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify")
] 