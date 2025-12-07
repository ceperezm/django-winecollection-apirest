from rest_framework import serializers, generics
from .models import Client, Provider, City
from django.contrib.auth.password_validation import validate_password

class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'username', 'birth_date', 'registration_date', 'email', 'password','password2'] 
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        client = Client.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            birth_date=validated_data['birth_date'],
            email=validated_data['email']
        )
        client.set_password(validated_data['password'])
        client.save()
        return client
        
        
        
class ProviderSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    class Meta:
        model = Provider
        fields = ['name', 'description', 'phone_number', 'identifier_number', 'city', 'email', 'password','password2']  
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        provider = Provider.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            phone_number=validated_data['phone_number'],
            identifier_number=validated_data['identifier_number'],
            city=validated_data['city_id'],
            email=validated_data['email']
        )
        provider.set_password(validated_data['password'])
        provider.save()
        return provider
                  