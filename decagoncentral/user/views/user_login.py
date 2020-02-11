from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework import status, permissions
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from ..serializers import LoginSerializer, TokenSerializer
from ..models.user_model import UserModel

# JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserLogin(APIView):
    # permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    # serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        user_username = request.data.get("username", "")
        user_password = request.data.get("password", "")

        user = authenticate(request, username=user_username, password=user_password)
        
        print(user)
        if user is not None:
            # LOGIN SAVES USER'S ID IN THE SESSION
            login(request, user)
            serializer = TokenSerializer(data={
                # USING DRF JWT UTILITY FUNCTIONS TO GENERATE A TOKEN
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})  
            serializer.is_valid()
            # data = serializer.data
            # resp = f"Welcome {data['username']}"
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)