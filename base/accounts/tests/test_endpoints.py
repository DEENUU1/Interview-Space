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


class LoginEndpointTestCase(APITestCase):
    def test_login_without_data(self) -> None:
        url = reverse('accounts:login')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LogoutEndpointTestCase(APITestCase):
    def test_logout(self) -> None:
        url = reverse('accounts:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


