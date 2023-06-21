from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import status


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        else:
            return Response(meesage='Registration Error', status=status.HTTP_400_BAD_REQUEST)
    
class UserDelete(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        #token = request.COOKIES.get('jwt')
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.get(id=payload['id'])
        print("@@@@@@@")
        print(user)
        user.delete()
        return Response({'message': 'User deleted!!!'})
    
    
class UserLogin(APIView):
    def post(self, request):
        email=request.data['email']
        password = request.data['password']
        
        # Add any additional validations as per your requirements (e.g., check email format)
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id' :user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
            
        }
        token=jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.data={'message': 'Login Success','jwt':token}
        response.set_cookie(key='jwt', value=token, httponly=True)
        print(response.data)
        return response

class UserView(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        #token = request.COOKIES.get('jwt')
        
        #print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!!!!')
        
        user = User.objects.get(id=payload['id'])
        if user:
            serializer=UserSerializer(user)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response({'message': 'User not found!!!'})



class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Successfully Logged out',
        }        
        return response
    
class UserEdit(APIView):
    #permission_classes = [IsAuthenticated]

    def put(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.get(id=payload['id'])
        
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated!!!'})
        return Response(serializer.errors, status=400)