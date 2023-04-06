from rest_framework.test import APITestCase
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
        cls.user = User.objects.create_user(email="test@example.com", username='userr', password='test123')
        cls.token = Token.objects.create(user=cls.user)
        cls.api_key = cls.token.key

class LevelListTestCase(BaseTestCase):
    def test_level_list_with_api_key_auth(self) -> None:
        url = reverse('api:level-list')
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_level_list_without_api_key_auth(self) -> None:
        url = reverse('api:level-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_level_list_with_invalid_api_key_auth(self) -> None:
        url = reverse('api:level-list')
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class QuestionListTestCase(BaseTestCase):
    def test_question_list_with_api_key_auth(self) -> None:
        url = reverse('api:question-list')
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_question_list_without_api_key_auth(self) -> None:
        url = reverse('api:question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_question_list_with_invalid_api_key_auth(self) -> None:
        url = reverse('api:question-list')
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class QuestionDetailsTestCase(BaseTestCase):
    def test_question_details_without_api_key_auth(self) -> None:
        pk = 1
        url = reverse('api:question-details', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_question_details_with_invalid_api_key_auth(self) -> None:
        pk = 1
        url = reverse('api:question-details', args=[pk])
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
