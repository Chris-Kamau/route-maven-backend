from django.shortcuts import render, redirect
from rest_framework import viewsets, generics, status
from .serializers import TodoSerializer, user_serializer
from rest_framework.views import APIView
from .models import Todo, Staff
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')

        # Check if the passwords match
        if password != password_confirmation:
            return Response({'message': 'Password and confirmation do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password using Django's make_password function
        hashed_password = make_password(password)

        # Create a new user with the hashed password
        user = User(username=username, password=hashed_password)
        user.save()

        return Response({'message': 'Registration successful.'})

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if request.user.is_authenticated:
                # Clear the existing session
                logout(request)

            # Log in the user
            login(request, user)
            return Response({'message': 'Login successful.'})
        else:
            return Response({'message': 'Login failed.'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    def get(self, request):
        # Log the user out
        logout(request)
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)

# def insertData(request):
#     if request.method == "POST":
#         driver_name = request.POST.get('driver_name')
#         image = request.POST.get('image')
#         number_plate = request.POST.get('number_plate')
#         driver_contact = request.POST.get('driver_contact')
#         gender = request.POST.get('gender')
#         #print details
#         query = Todo(driver_name=driver_name, image=image, number_plate=number_plate, driver_contact=driver_contact, gender=gender)
#         query.save()
#         return redirect("api/form/")
    

# def Signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()



