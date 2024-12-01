from django.shortcuts import render
# Only for get functionality
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# For POST functionality

from rest_framework import status  # List of status code when returning responses from the API
from profiles_api import serializers  # serializers created in app


class HelloApiView(APIView):  # Creates a new class based on ApiView and allows to define the application logic for our
    # endpoints we can assign to this view and call the appropriate function
    """Test ApiView"""
    # For Post
    serializer_class = serializers.HelloSerializer  # Expect an i/p of name

    def get(self, request, format=None):  # retrieve a list or specific object
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
        return Response({'message': 'Hello',
                         'an_apiview': an_apiview})  # contains dictionary and rest_framework converts it to a json

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(
            data=request.data)  # serializer_class() comes with the APIVIew which retrieve the configured serializer class for our view.
        # When you make a post request to our APIView the data going to pass in as request.data which is part of the request object
        # We assign the data to our serializer_class
        # validate the serializer for i/p
        if serializer.is_valid():  # function used to check serializer is valid means max_length=10
            name = serializer.validated_data.get('name')  # This retrieve the name field we defined in serializer
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors,
                            # errors generated by the serializer. This will give a dictionary of all the errors based on the validation rule applied
                            status=status.HTTP_400_BAD_REQUEST)  # by default it return 200 ok. override to get a bad request

    def put(self, request, pk=None):  # pk take id of the object to be updated
        """Handle updating an entire object"""
        return Response({"methods": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object. Only update the fields provided in the request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})
