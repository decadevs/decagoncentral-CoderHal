from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .mock_data.user_data import user_data
from ..models import User
# Create your tests here.


class TestUserView(APITestCase):
    ''' Tests for different endpoints'''

    def setUp(self):
        User.objects.create(**user_data())
        self.url = reverse('user')+'?username=osy' 

    def test_api_can_create_user(self):

        url = reverse("users")
        response= self.client.post(url, user_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], user_data()['name'])


    def test_api_can_get_a_user(self):
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

