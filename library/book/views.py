from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import views

from .serializer import BookSerializer
from .models import Book




# Create your views here.
#
# @api_view(['GET'])
# def getBook(request):
#     books =[
#         {
#             "id":1,
#             "title":"Introduction to Python"
#
#         },
#         {
#             "id": 2,
#             "title": "Introduction to java"
#         },
#         {
#             "id": 3,
#             "title": "Introduction to Graphic Design"
#         }
#
#     ]
#     return Response(books, status=status.HTTP_200_OK)


class BookCreateLiist(APIView):

    def get(self,request, format= None):
        book = Book.objects.all()
        book_json = BookSerializer(book, many=True)
        return Response(book_json.data, status= status.HTTP_200_OK)

    def post(self,request, format=None):
        serializeeer = BookSerializer(data=request.data)
        if serializeeer.is_valid():
            serializeeer.save()
            return Response(serializeeer.data, status.HTTP_200_OK)
        return Response(serializeeer.errors, status.HTTP_400_BAD_REQUEST)