from django.urls import path
from . import views




urlpatterns = [
    path("all/<int:user>", views.SubscriptionView.as_view(), name="subscription_all"),
    path("create/", views.SubscriptionView.as_view(), name="subscription_create"),
    path("delete/", views.SubscriptionView.as_view(), name="subscription_delete")

]

