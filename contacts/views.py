from rest_framework import generics
from contacts.models import Contacts
from rest_framework.permissions import IsAuthenticated

from contacts.serializers import ContactSerializer

class ContactsView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    permission_classes = (IsAuthenticated,)
    
    # set the user to the current logged in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

    def get_queryset(self):
        return Contacts.objects.filter(user=self.request.user)



class ContactsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'id'


    def get_queryset(self):
        return Contacts.objects.filter(user=self.request.user)