from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """
    Test API View
    """
    def get(self,request, format=None):
        """
        Returns a list of APIView Features
        """
        an_apiview = [
        'Uses HTTP methods as funtion (get, put, post,patch,delete)',
        'Gives most control over your logic',
        'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
