from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .contactSerializer import ContactSerializer
from .models import Contact

# Create your views here.

class ContactCreateList(APIView):
    def get(self, request, format=None):
        contact = Contact.objects.all()
        contact_json = ContactSerializer(contact, many=True)
        return Response(contact_json.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        contact2 = ContactSerializer(data=request.data)
        if contact2.is_valid():
            contact2.save()
            return Response(contact2.data, status.HTTP_200_OK)
        return Response(contact2.errors, status.HTTP_400_BAD_REQUEST)