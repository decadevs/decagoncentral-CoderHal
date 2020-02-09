from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from ..serializers import UserSerializer 
from ..models.users import User


class UserDetail(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise("Kindly Signup")
    
    def get(self, request):
        user_username = request.GET.get("username")
        user = User.objects.get(username=user_username)
        serializer = UserSerializer(user)
        data = serializer.data
        resp = f"Welcome {data['username']}"
        return Response(resp)