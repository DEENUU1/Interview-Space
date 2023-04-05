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
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if len(password) <= 8:
        return Response({'error': "Password is too short. Your password should have at least 8 characters."})
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'success': True})


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'success': True})
    else:
        return Response({'success': False, 'error': 'Invalid credentials'})


@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response({'success': True})


@api_view(['GET'])
def profile_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({'Your username': user.username})
    return Response({"error": "You are not logged in."})