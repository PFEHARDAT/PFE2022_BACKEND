from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics, status
from .serializers import SubscribeToUserSerializer
from .models import Subscription
from usersApp.models import User
from followersApp.models import Follower


# Create your views here.

class SubscriptionView(APIView):
    serializer_class = SubscribeToUserSerializer
    def get(self, request:Request, user):
        subscriptions = Subscription.objects.all().filter(user=user)
        serializer = SubscribeToUserSerializer(subscriptions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request:Request):
        user = request.data.get("user")
        data = request.data
        subscription = Subscription.objects.filter(user=user, subscription=request.data.get("subscription"))
        serializer = self.serializer_class(data=data)
        if subscription.exists():
            subscription.delete()
            self.updateSubscriptionsCount(user, False)
            self.updateFollowerCount(subscription, False)
            self.deleteFromFollower(subscription, user)
        elif serializer.is_valid():
            serializer.save()
            self.updateSubscriptionsCount(user, True)
            self.updateFollowerCount(request.data.get("subscription"), True)
            self.addToFollower(request.data.get("subscription"), user)
            response = {"message": "Subscription Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #def delete(self, request:Request):
    #    user = request.data.get("user")
    #    subscription = request.data.get("subscription")
    #    subscription_exist = Subscription.objects.filter(user=user, subscription=subscription)
    #    subscription_exist.delete()
    #    self.updateSubscriptionsCount(user, False)
    #    self.updateFollowerCount(subscription, False)
    #    return Response(data='DELETED', status=status.HTTP_200_OK)
    
    def updateSubscriptionsCount(self, user, increment):
        user = User.objects.get(id=user)
        if increment :
            user.following_count += 1
        else:
            user.following_count -= 1
        user.save()
    def updateFollowerCount(self, user, increment):
        user = User.objects.get(id=user)
        if increment :
            user.followers_count += 1
        else:
            user.followers_count -= 1
        user.save()
    def addToFollower(self, user, follower):
        Follower.objects.create(user=user, follower=follower)
    def deleteFromFollower(self, user, follower):
        follower = Follower.objects.filter(user=user, follower=follower)
        follower.delete()









