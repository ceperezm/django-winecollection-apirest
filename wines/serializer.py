from rest_framework import serializers

from .models import Wine, Attribute

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields =['name','description','harvest year','maker','variety','attribute', 'city']
        
class AttributteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['total_sulfur_dioxide', 'fixed_acidity', 'volatile_acidity', 'free_sulfur_dioxide', 'citric_acid', 'residual_sugar', 'chlorides', 'density', 'pH', 'sulphates', 'alcohol']
        
        
        