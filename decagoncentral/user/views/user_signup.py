from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from ..serializers import SignupSerializer 
from ..models.user_model import UserModel


class UserSignup(APIView):
    queryset = UserModel.objects.all()
    serializer_class = SignupSerializer
    
    def post(self, request, format=None):
        ''' creates a new user'''
        fullname = request.data.get("fullname", "")
        username = request.data.get("username", "")
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        position = request.data.get("position", "")

        if not fullname or not username or not email or not password or not position:
            return Response(
                data = {
                    "message": "All fields required!"
                },
                status = status.HTTP_400_BAD_REQUEST
            )
        new_user = UserModel.objects.create(
            fullname = fullname,
            username = username,
            email = email,
            password = password,
            position = position

        )
        resp = f"Welcome {username}"
        return Response(resp, status=status.HTTP_201_CREATED)