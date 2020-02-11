from rest_framework import serializers
from ..models import UserModel

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)