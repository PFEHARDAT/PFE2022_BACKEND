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
from followersApp.views import FollowerView

# Create your views here.

class SubscriptionView(APIView):
    serializer_class = SubscribeToUserSerializer
    def get(self, request:Request, user):
        subscriptions = Subscription.objects.all().filter(user=user)
        serializer = SubscribeToUserSerializer(subscriptions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request:Request):
        user = request.data.get("user")
        subscription = request.data.get("subscription")
        print(request.data)
        data = request.data
        print("----")
        print("----")

        serializer = self.serializer_class(data=data)
        print(serializer)
        # print("----")

        # print(serializer.data)
        print("----")
        print("----")
        
        if serializer.is_valid():
            print("==>  rentré dans if")
            serializer.save()
            self.updateSubscriptionsCount(user, True)
            url("followers/create/", )
            response = {"message": "Subscription Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        # subscription_exist = Subscription.objects.filter(user=user, subscription=subscription)
        # subscription_exist.delete()
        # self.updateSubscriptionsCount(user, False)
        # self.updateFollowerCount(subscription_exist, False)
        # self.deleteFromFollower(subscription_exist, user)
        print("hello world")
        return Response(data='DELETED', status=status.HTTP_200_OK)       


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
        print("user that make the action => ", user)
        # if increment :
        #     user.following_count += 1
        # else:
        #     user.following_count -= 1
        # user.save()
    def updateFollowerCount(self, user, increment):
        user = User.objects.get(id=user)
        print("followed user=> ", user)
        # if increment :
        #     user.followers_count += 1
        # else:
        #     user.followers_count -= 1
        # user.save()
    def addToFollower(self, user, follower):
        
        print(">>> In addToFollower(self, user, follower):")
        print("- user:", user.id)
        print("- follower:", follower.id)    

        Follower.objects.create(user=user, follower=follower)
    def deleteFromFollower(self, user, follower):
        follower = Follower.objects.filter(user_id=user, follower=follower)
        follower.delete()
        









