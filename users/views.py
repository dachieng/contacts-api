import jwt
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from users.serializers import RegisterUserSerializer, LoginSerializer


class AuthUserView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

class LoginUserView(generics.GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self,request, *args, **kwargs):
        data = request.data
        username = data.get('username','')
        password = data.get('password','')

        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode({'username':user.username}, settings.SECRET_KEY)
    
        # set up the serializer

            serializer = self.get_serializer(user)

            data = {
                'user':serializer.data,
                'token': auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'errors':'invalid_credentials'}, status=status.HTTP_401_UNAUTHORIZED)

