from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from rest_framework.response import Response
# from rest_framework_jwt.settings import api_settings

import bcrypt

from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import LoginSerializer, TokenSerializer
from ..models.user_model import UserModel

class UserLogin(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        user_username = request.data.get("username", '')
        user_password = request.data.get("password", '')
        # user_password.encode('utf-8')
        if not user_username and not user_password:
            return Response({'error': 'All fields required!'}, status=status.HTTP_400_BAD_REQUEST)

        user = UserModel.objects.get(username=user_username)
        if user is not None: 

            serializer = LoginSerializer(user)
            data = serializer.data
            saved_password = data['password']
# 
            if bcrypt.checkpw(b'user_password', saved_password):

                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)

                resp = f"Welcome, {data['username']}, your token is {access}!"
                return Response(resp, status=status.HTTP_200_OK)
            return Response("Username or password not correct!", status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_404_NOT_FOUND)