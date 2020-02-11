from django.urls import path
from .views import UserLogin, UserSignup

urlpatterns = [
    path('auth/signup/', UserSignup.as_view(), name='usersignup'),
    path('auth/login/', UserLogin.as_view(), name='userlogin'),
]
