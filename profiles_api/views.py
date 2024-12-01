from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView): #Creates a new class based on ApiView and allows to define the application logic for our
                            # endpoints we can assign to this view and call the appropriate function
    """Test ApiView"""
    def get(self, request, format=None): #retrieve a list or specific object
        """Returns a list of APIView features
        request - object passed by rest framework and contains details about the request being made to the api.
        format - format suffix to the end of the URL , best practice """
        an_apiview = [
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLS',
        ]
        # must return a response object
        return Response({'message' : 'Hello', 'an_apiview': an_apiview}) # contains dictionary and rest_framework converts it to a json

