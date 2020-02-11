from rest_framework import serializers
from ..models import UserModel

class SignupSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = UserModel
        fields = ('fullname', 'username', 'email', 'password', 'position')

