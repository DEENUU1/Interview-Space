from rest_framework import generics, permissions
from .models import Level, ProgrammingLang, Question, Comment, Favourite, Category
from .serializers import (
    LevelModelSerializer,
    ProgrammingLangModelSerializer,
    QuestionModelSerializer,
    CommentModelSerializer,
    FavouriteModelSerializer,
    CategoryModelSerializer,

)
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response


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


class CategoryList(generics.ListAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Category.objects.all()
        else:
            return None


class QuestionList(generics.ListAPIView):
    """
    /questions/?level=X&lang=X&api_key=X
    """
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):
        queryset = Question.objects.all()
        level = self.request.query_params.get('level', None)
        programming_lang = self.request.query_params.get('lang', None)
        category = self.request.query_params.get('category', None)
        api_key = self.request.query_params.get('api_key', None)
        
        if api_key is None:
            return queryset.none() 
        if level is not None:
            queryset = queryset.filter(level=level)
        if programming_lang is not None:
            queryset = queryset.filter(programming_lang=programming_lang)
        if category is not None:
            queryset = queryset.filter(category=category)
            
        return queryset
    

class QuestionCreateView(generics.CreateAPIView):
    """
    
    """
    serializer_class = QuestionModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ProgrammingLangList(generics.ListAPIView):
    """

    """
    queryset = ProgrammingLang.objects.all()
    serializer_class = ProgrammingLangModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return ProgrammingLang.objects.all()
        else:
            return None


class CommentList(generics.ListAPIView):
    """
    
    """
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        question = self.request.query_params.get('question', None)
        api_key = self.request.query_params.get('api_key', None)
        
        if api_key is None:
            return queryset.none() 
        if question is not None:
            queryset = queryset.filter(question=question)
    
        return queryset


class CommentCreate(generics.CreateAPIView):
    """
    
    """
    serializer_class = CommentModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Question.objects.filter(id=question_id)


class AddToFavourite(generics.CreateAPIView):
    """
    
    """
    serializer_class = FavouriteModelSerializer

    def get_object(self):
        question_id = self.kwargs.get('question_id')
        return generics.get_object_or_404(Question, id=question_id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, question=self.get_object())


class FavouriteDelete(generics.DestroyAPIView):
    queryset = Favourite.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            favourite = self.queryset.get(user=request.user, question_id=kwargs['question_id'])
            favourite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "Favourite not found"}, status=status.HTTP_404_NOT_FOUND)
