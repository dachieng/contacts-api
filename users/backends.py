import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions

# setting up an authentication scheme for user during login

class JWTAuthentication(authentication.BaseAuthentication):
    
    # override the authenticate method

    def authenticate(self, request):
        # get the headers
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        # get the bearer and token
        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY,algorithms="HS256")
            user = User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid')
        except jwt.ExpiredSignature as identifier:
            raise exceptions.AuthenticationFailed('Your token has expired')
        return super().authenticate(request)