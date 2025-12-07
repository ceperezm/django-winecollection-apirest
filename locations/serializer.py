from rest_framework import serializers
from .models import Country, City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']
        
class CitySerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField( slug_field='name', queryset=Country.objects.all()) # Use country name instead of ID for representation
    
    class Meta:
        model = City
        fields = ['name', 'country_id']
        
                