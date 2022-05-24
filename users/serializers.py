import email

from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length =8, max_length=65, write_only = True)
    email = serializers.CharField(min_length = 3, max_length=255)
    first_name = serializers.CharField(min_length = 3, max_length=255)
    last_name = serializers.CharField(min_length = 3, max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    # called before an instance is created
    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'Email already exists'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':'Username already exists'})
        return super().validate(attrs)

    # creates the user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length =8, max_length=65, write_only = True)
    username = serializers.CharField(min_length = 3, max_length=255)

    class Meta:
        model = User
        fields = ['username','password']

