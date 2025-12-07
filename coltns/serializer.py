from rest_framework import serializers
from .models import ClientCollection,ProviderCollection,ClientCollectionWine,ProviderCollectionWine,Type,ProviderWine

class ProviderCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCollection
        fields = ['collection_name', 'description', 'registration_date', 'provider_id', 'type_id']
        
        
class ProviderWineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderWine
        fields = ['provider_id', 'wine_id', 'added_date']
        
class ClientCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCollection
        fields = ['collection_name', 'description', 'registration_date', 'client_id']  
        
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['type_name', 'description']
        

class ClientCollectionWineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCollectionWine
        fields = ['client_collection_id', 'wine_id', 'added_date']
        
class ProviderCollectionWineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCollectionWine
        fields = ['provider_collection_id', 'wine_id', 'added_date']
                                                        