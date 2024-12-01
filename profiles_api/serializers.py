from rest_framework import serializers

class HelloSerializer(serializers.Serializer): #Serializer is a class here, It will accept a name i/p and add this to APIView to test POST functionality
    """Serializers a name field for testing our APIView also can be used as a validator"""
    name = serializers.CharField(max_length=10)

