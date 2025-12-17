from rest_framework import serializers
from .models import Wine, Attribute
from locations.models import City
from locations.serializer import CitySerializer
       
class AttributeSerializer(serializers.ModelSerializer):
    """Serializer for wine attributes."""
    class Meta:
        model = Attribute
        fields = [
            'id',
            'total_sulfur_dioxide',
            'fixed_acidity',
            'volatile_acidity',
            'free_sulfur_dioxide',
            'citric_acid',
            'residual_sugar',
            'chlorides',
            'density',
            'pH',
            'sulphates',
            'alcohol'
        ]
        read_only_fields = ['id']
        
class WineReadSerializer(serializers.ModelSerializer):
    """Serializer for reading wine data."""
    attribute = AttributeSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    
    class Meta:
        model = Wine
        fields = [
            'id',
            'name',
            'harvest_year',
            'variety',
            'attribute',
            'city',
            'created_at',
            'updated_at'
        ]
       
class WineWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating wine data."""
    attribute = AttributeSerializer()
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )
    
    class Meta:
        model = Wine
        fields = [
            'id',
            'name',
            'harvest_year',
            'variety',
            'attribute',
            'city_id'
        ]    
        read_only_fields = ['id']            
        
    def create(self, validated_data):
        attribute_data = validated_data.pop('attribute')
        attribute = Attribute.objects.create(**attribute_data)
        wine = Wine.objects.create(attribute=attribute, **validated_data)
        return wine
        
    def update(self, instance, validated_data):
        attribute_data = validated_data.pop('attribute', None)
        if attribute_data:
            attribute_serializer = AttributeSerializer(instance.attribute, data=attribute_data)
            if attribute_serializer.is_valid(raise_exception=True):
                attribute_serializer.save()
        return super().update(instance, validated_data)