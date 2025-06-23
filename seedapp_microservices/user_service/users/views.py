from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import  *
from .models import *
from django.contrib.auth.hashers import check_password

class SignupUserAPI(APIView):
    def post(self, request):
        data = request.data
        if 'phone' not in data:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        if Userlogin.objects.filter(phone=data['phone']).exists():
            return Response({'error': 'Phone number is already registered'}, status=status.HTTP_400_BAD_REQUEST)
        
      
        serializer = UserloginSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  
            return Response({
                'message': 'User signed up successfully',
                 'redirect_to': '/home'
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'error': 'Invalid data',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class LoginUserAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  
        if not serializer.is_valid():
            return Response({
                'status': 'error',
                'message': 'Invalid input',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

       
        phone = serializer.validated_data.get('phone')
        password = serializer.validated_data.get('password')
        user_login = Userlogin.objects.filter(phone=phone).first()
        if not user_login:
            return Response({
                'status': 'error',
                'message': 'Invalid phone number or password'
            }, status=status.HTTP_401_UNAUTHORIZED) 
        user = user_login.user
        
        if user and check_password(password, user.password): 
         
            return Response({
                'status': 'success',
                'message': 'Login successful',
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'phone': phone
                },
                'redirect_to': '/home'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'error',
            'message': 'Invalid phone number or password'
        }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserAPI(APIView):
    def post(self, request):
        request.session.flush()  
        
        response_data = {
            'message': 'Logout successful',
            'redirect_to': '/home'  
        }

        return Response(response_data, status=status.HTTP_200_OK)
