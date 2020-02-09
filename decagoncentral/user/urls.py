from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('user/', UserDetail.as_view(), name='user'),
]
