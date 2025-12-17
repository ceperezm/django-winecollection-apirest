from rest_framework import serializers
from .models import Country, City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']
        
class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    class Meta:
        model = City
        fields = ['name', 'country_id']
                     