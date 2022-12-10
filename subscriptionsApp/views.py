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
    permission_classes = []
    def get_all_subscription(self, user):
        subscriptions = Subscription.objects.all().filter(user=user)
        return subscriptions

class SubscribeToUserView(APIView):
    permission_classes = []
    serializer_class = SubscribeToUserSerializer
    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            instance = serializer.save(commit=False)
            instance.user = request.user
            instance.subscritpion = request.subscription
            response = {"message": "Subbscription Created Successfully", "data": instance.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)









