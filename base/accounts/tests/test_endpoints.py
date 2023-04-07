from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class RegisterEndpointTestCase(APITestCase):
    def test_register_with_valid_data(self) -> None:
        url = reverse('accounts:register')
        data = {'username': 'testuser',
                'email': 'testuser@example.com',
                 'password': 'test1234' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_register_with_invalid_data(self) -> None:
        url = reverse('accounts:register')
        data = {'username': 'testuser',
                'email': 'testuser@example.com',
                 'password': 'test' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, {'error': "Password is too short. Your password should have at least 8 characters."} )