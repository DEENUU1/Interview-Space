from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def register_view(request):
    """
    A view for registering a new user. It takes a POST request with the following parameters in the request body:

    'username': The desired username for the new user.
    'email': The email address for the new user.
    'password': The desired password for the new user. The password must be at least 8 characters long.
    """
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if len(password) <= 8:
        return Response({'error': "Password is too short. Your password should have at least 8 characters."})
    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'success': True})


@api_view(['POST'])
def login_view(request):
    """
    A view for logging in a user. It takes a POST request with the following parameters in the request body:

    'username': The username of the user trying to log in.
    'password': The password of the user trying to log in.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'success': True})
    else:
        return Response({'success': False, 'error': 'Invalid credentials'})


@api_view(['POST'])
def logout_view(request):
    """ 
    A view for logging out a user. It takes a POST request and logs out the currently logged-in user.
    """
    logout(request)
    return Response({'success': True})


@api_view(['GET'])
def profile_view(request):
    """ 
    A view for retrieving the profile of the currently logged-in user. It takes a GET request and returns a JSON response
    """
    user = request.user

    if user.is_authenticated:
        return Response({'Your username': user.username})
    return Response({"error": "You are not logged in."})