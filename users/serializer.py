from rest_framework import serializers
from .models import Client, Provider

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'birth_date', 'registration_date', 'email']
        
        
        
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'description', 'phone_number', 'identifier_number', 'city_id', 'registration_date', 'email']