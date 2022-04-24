from django.shortcuts import render

from .serializers import flyserializer
from rest_framework.response import responses
from  rest_framework import  viewsets


# Create your views here.
class flyviewset(viewsets.viewset):
    def list(self, request):
        username = request.headers.get("username")
        token = request.headers.get("tocken")
        print(username)
        print(token)



     def create(self,request):
         pass