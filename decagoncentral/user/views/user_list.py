from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from ..serializers import UserSerializer 
from ..models.users import User


class UserList(APIView):
    
    def post(self, request, format=None):
        ''' creates a new user'''
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            resp = f"Dear {user.username}, your registration is successful"
            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)