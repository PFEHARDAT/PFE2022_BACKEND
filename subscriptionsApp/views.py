from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics, status
from .serializers import AllSubscriptionSerializer
from .serializers import SubscribeToUserSerializer

# Create your views here.

class AllSubscriptionView(APIView):
    serializer_class = AllSubscriptionSerializer
    def get(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        response = {"message": "get All susbcription by user", "data": serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)

class SubscribeToUserView(APIView):
    serializer_class = SubscribeToUserSerializer
    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Subbscription Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)









