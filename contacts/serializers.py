from rest_framework import serializers
from contacts.models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'country_code', 'first_name', 'last_name', 
            'phone_number', 'profile_picture', 'is_favorite']


