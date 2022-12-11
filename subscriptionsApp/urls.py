from django.urls import path
from . import views




urlpatterns = [
    path("all/<int:user>", views.AllSubscriptionView.as_view(), name="subscription_all"),
    path("create/<int:user>", views.SubscribeToUserView.as_view(), name="subscription_create")
]

