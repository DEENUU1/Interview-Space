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
from rest_framework.authentication import SessionAuthentication


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
    A view that returns a list of levels and their details, optionally filtered by an API key.  
    Attributes:
        queryset (QuerySet): The query set used to retrieve levels from the database.
        serializer_class (LevelModelSerializer): The serializer used to convert level instances
            to JSON format.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the API key in the request.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.
        pagination_class (ApiPagination): The pagination class used to paginate the response.

    Methods:
        get_queryset(self): Returns the query set to use for this view. If an API key is present
            in the request, the full list of levels is returned. Otherwise, an empty list is returned.
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
    A view that returns a list of categories and their details, optionally filtered by an API key.

    Attributes:
        queryset (QuerySet): The query set used to retrieve categories from the database.
        serializer_class (CategoryModelSerializer): The serializer used to convert category instances
            to JSON format.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the API key in the request.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.
        pagination_class (ApiPagination): The pagination class used to paginate the response.

    Methods:
        get_queryset(self): Returns the query set to use for this view. If an API key is present
            in the request, the full list of categories is returned. Otherwise, an empty list is returned.
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
    A view that returns a list of questions and their details, filtered by level, programming language,
    category and optionally, an API key.

    Attributes:
        queryset (QuerySet): The query set used to retrieve questions from the database.
        serializer_class (QuestionModelSerializer): The serializer used to convert question instances
            to JSON format.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the API key in the request.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.
        pagination_class (ApiPagination): The pagination class used to paginate the response.

    Methods:
        get_queryset(self): Returns the query set to use for this view. If an API key is not present
            in the request, an empty queryset is returned. Otherwise, the queryset is filtered based
            on the specified query parameters, which include `level`, `lang` (for programming language),
            and `category`.
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


class QuestionDetail(generics.RetrieveAPIView):
    """
    A view that returns the details of a single question, identified by its primary key (id).
    
    Attributes:
        queryset (QuerySet): The query set used to retrieve questions from the database.
        serializer_class (QuestionModelSerializer): The serializer used to convert question instances
            to JSON format.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the API key in the request.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.

    Methods:
        dispatch(self, request, *args, **kwargs): Handles incoming requests and dispatches them to the
            appropriate handler method (`get` for retrieving details of a single question). Calls the
            parent class method to perform the actual dispatch.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class QuestionCreateView(generics.CreateAPIView):
    """
    A view that handles the creation of a new question.

    Attributes:
        serializer_class (QuestionModelSerializer): The serializer used to convert JSON data in the
            request to a question instance for saving in the database.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the session in the request.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.

    Methods:
        post(self, request, *args, **kwargs): Handles POST requests and creates a new question
            instance in the database based on the JSON data in the request body. Returns a JSON
            representation of the newly created question, including its assigned ID.
    """

    serializer_class = QuestionModelSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ProgrammingLangList(generics.ListAPIView):
    """
    A view that returns a list of all available programming languages.

    Attributes:
        queryset (QuerySet): The query set used to retrieve programming languages from the database.
        serializer_class (ProgrammingLangModelSerializer): The serializer used to convert programming
            language instances to JSON format.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the API key in the request.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.
        pagination_class (ApiPagination): The pagination class used to paginate the results.

    Methods:
        get_queryset(self): Returns the query set of all programming languages in the database, or
            None if the API key is not provided in the request.
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
    A view that returns a list of comments associated with a particular question.

    Attributes:
    queryset (QuerySet): The query set used to retrieve comments from the database.
    serializer_class (CommentModelSerializer): The serializer used to convert comment instances to
        JSON format.
    authentication_classes (tuple): A tuple containing the authentication class used to verify
        the API key in the request.
    permission_classes (tuple): A tuple containing the permission classes required to access
        this view.

    Methods:
        get_queryset(self): Returns the query set of comments associated with a particular question.
            The question ID is taken from the `pk` parameter in the URL. If the API key is not provided
            in the request, an empty query set is returned.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        pk = self.kwargs['pk']
        api_key = self.request.query_params.get('api_key', None)
        
        if api_key is None:
            return queryset.none() 
        if pk is not None:
            queryset = queryset.filter(question=pk)
    
        return queryset


class CommentCreate(generics.CreateAPIView):
    """
    A view that creates a new comment associated with a particular question.

    Attributes:
        serializer_class (CommentModelSerializer): The serializer used to validate the request data and
            create a new comment instance.
        authentication_classes (tuple): A tuple containing the authentication class used to verify
            the user session.
        permission_classes (tuple): A tuple containing the permission classes required to access
            this view.

    Methods:
        get_queryset(self): Returns the query set of questions associated with a particular ID. The
            question ID is taken from the `question_id` parameter in the URL.
    """

    serializer_class = CommentModelSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Question.objects.filter(id=question_id)


class AddToFavourite(generics.CreateAPIView):
    """
    A view that adds a particular question to the list of user's favorites.

    Authentication is required to access this view. The currently logged-in user is assigned to the
    `user` field of the favorite instance, and the question being added is assigned to the `question`
    field, extracted from the `question_id` parameter in the URL.

    Attributes:
        serializer_class (FavouriteModelSerializer): The serializer used to validate the request data
            and create a new favorite instance.

    Methods:
        get_object(self): Returns the question object with the ID specified in the URL. If the object
            does not exist, a 404 error is raised.
        perform_create(self, serializer): Overrides the default implementation to set the user and
            question fields of the favorite instance and save it to the database.
    """
    serializer_class = FavouriteModelSerializer

    def get_object(self):
        question_id = self.kwargs.get('question_id')
        return generics.get_object_or_404(Question, id=question_id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, question=self.get_object())


class FavouriteDelete(generics.DestroyAPIView):
    """ 
    Deletes a favorite question for the authenticated user.
    If the favorite question is successfully deleted, returns an HTTP 204 No Content response.
    If the favorite question is not found, returns an HTTP 404 Not Found response.
    """

    queryset = Favourite.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            favourite = self.queryset.get(user=request.user, question_id=kwargs['question_id'])
            favourite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "Favourite not found"}, status=status.HTTP_404_NOT_FOUND)
