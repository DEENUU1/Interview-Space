from rest_framework import generics, permissions
from .models import Level, ProgrammingLang, Question, Comment, Favourite
from .serializers import (
    LevelModelSerializer,
    ProgrammingLangModelSerializer,
    QuestionModelSerializer,
    CommentModelSerializer,
    FavouriteModelSerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.pagination import PageNumberPagination


class ApiKeyAuthentication(TokenAuthentication):
    """
    This authentication class extends the TokenAuthentication class
    to allow authentication using API keys passed as query parameters
    in the request URL.
    """

    def authenticate(self, request):
        api_key = request.query_params.get('api_key')
        if not api_key:
            return None
        try:
            token = Token.objects.get(key=api_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')

        return (token.user, token)


class ApiPagination(PageNumberPagination):
    """
    A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    This class is designed to handle paginated responses for API views. It sets the default page size to 2 but can be
    customized by setting the page_size attribute.
    Attributes:
    page_size (int): The number of items to include on each page. Defaults to 2.
    """
    page_size = 10


class LevelList(generics.ListAPIView):
    """

    """
    queryset = Level.objects.all()
    serializer_class = LevelModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Level.objects.all()
        else:
            return None
