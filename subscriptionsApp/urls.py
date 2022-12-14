from django.urls import path
from . import views




urlpatterns = [
    path("all/<int:user>", views.SubscriptionView.as_view(), name="subscription_all"),
    path("create/", views.SubscriptionView.as_view(), name="subscription_create"),
    path("delete/<int:user>/<int:subscription>", views.SubscriptionView.as_view(), name="subscription_delete"),
    path("exist/<int:user>/<int:subscription>", views.ExistSubscriptionView.as_view(), name="subscription_exist")
]

