from django.urls import path
from . import views




urlpatterns = [
    path("/all/<int:user>", views.SubscriptionView.as_view(), name="subscription_all"),
    path("", views.SubscriptionView.as_view(), name="subscription_create"),
    path("/exist/<int:user>/<int:subscription>", views.ExistSubscriptionView.as_view(), name="subscription_exist")
]

