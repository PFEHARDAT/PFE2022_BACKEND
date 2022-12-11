from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics, status
from .serializers import SubscribeToUserSerializer
from .models import Subscription


# Create your views here.

class AllSubscriptionView(APIView):
    def get(self, request:Request, user):
        subscriptions = Subscription.objects.all().filter(user=user)
        serializer = SubscribeToUserSerializer(subscriptions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class SubscribeToUserView(APIView):
    serializer_class = SubscribeToUserSerializer
    def post(self, request:Request):
        user = request.data.get("user")
        subscription = request.data.get("subscription")
        data = request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Subbscription Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        subscription_exist = Subscription.objects.filter(user=user, subscription=subscription)
        subscription_exist.delete()
        return Response(data='DELETED', status=status.HTTP_200_OK)









