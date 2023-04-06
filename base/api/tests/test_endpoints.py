from rest_framework import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 



class BaseTestCase(APITestCase):
    @classmethod
    def setUp(cls) -> None:
        """
        Sets up the test data and creates a user and token objects for the test.
        """
        super().setUpClass()
        cls.user = User.objects.create_user(username='test', email='user@example.com', test='test123')
        cls.token = Token.objects.create(user=cls.user)


