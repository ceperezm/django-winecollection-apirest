from rest_framework import serializers
from .models import Wine, Attribute
from locations.models import City
from locations.serializer import CitySerializer
from django.core.validators import MinValueValidator, MaxValueValidator
       
class AttributeSerializer(serializers.ModelSerializer):
    total_sulfur_dioxide = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)])
    fixed_acidity = serializers.FloatField(validators=[MinValueValidator(5.0), MaxValueValidator(20.0)])
    volatile_acidity = serializers.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(2.0)])
    free_sulfur_dioxide = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(80)])
    citric_acid = serializers.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    residual_sugar =serializers.FloatField( validators=[MinValueValidator(0.5), MaxValueValidator(1.0)])
    chlorides =serializers.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    density =serializers.FloatField( validators=[MinValueValidator(0.9900), MaxValueValidator(1.0100)])
    pH =serializers.FloatField( validators=[MinValueValidator(2.0), MaxValueValidator(5.0)])
    sulphates =serializers.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(2.0)])
    alcohol =serializers.FloatField( validators=[MinValueValidator(5.0), MaxValueValidator(20.0)])
    class Meta:
        model = Attribute
        fields = ['total_sulfur_dioxide', 'fixed_acidity', 'volatile_acidity', 'free_sulfur_dioxide', 'citric_acid', 'residual_sugar', 'chlorides', 'density', 'pH', 'sulphates', 'alcohol']
        
  
class WineWriteSerializer(serializers.ModelSerializer):
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )
    attribute = AttributeSerializer()
    
    class Meta:
        model = Wine
        fields = ['name', 'description', 'harvest_year', 'maker', 'variety', 
                  'attribute', 'city_id']
        
    def validate(self, attrs): # Validation method to ensure unique wine entries
        
        name = attrs.get('name')
        harvest_year = attrs.get('harvest_year')
        maker = attrs.get('maker')
        
        if not self.instance:
            if Wine.objects.filter(
                name=name, 
                harvest_year=harvest_year,
                maker=maker
            ).exists():
                raise serializers.ValidationError({
                    'name': f'Ya existe un vino "{name}" del año {harvest_year} de {maker}'
                })
        
        return attrs    
    
    def create(self, validated_data):
        city = validated_data.pop('city')
        attribute_data = validated_data.pop('attribute')
        
        attribute = Attribute.objects.create(**attribute_data)
        wine = Wine.objects.create(
            attribute=attribute,
            city=city,
            **validated_data
        )
        return wine
    
    def update(self, instance, validated_data):
        attribute_data = validated_data.pop('attribute', None)
        city = validated_data.pop('city', None)
        
        if attribute_data:
            for attr, value in attribute_data.items():
                setattr(instance.attribute, attr, value)
            instance.attribute.save()
        
        if city:
            instance.city = city
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance



class WineReadSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    attribute = AttributeSerializer(read_only=True)
    
    class Meta:
        model = Wine
        fields = ['id', 'name', 'description', 'harvest_year', 'maker', 'variety','attribute', 'city']

       
        