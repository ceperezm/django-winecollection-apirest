from pyexpat import model
import comments
from rest_framework import serializers
from .models import WineComment, ClientCollectionCommment

class WineCommentReadSerializer(serializers.ModelSerializer):
    """Serializer for reading wine comments."""

    client = serializers.SlugRelatedField(slug_field='username', read_only=True)
    wine = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = WineComment
        
        fields = [
            'id',
            'client', # Who made the comment
            'wine', # Foreign key to Wine
            'comment',
            'comment_date',
        ]
        read_only_fields = fields

class WineCommentWriteSerializer(serializers.ModelSerializer):
    """Serializer for writing wine comments."""

    class Meta:
        model = WineComment
        fields =[
            'wine','comment'
        ]

    def validate_comment(self,value):
        if len(value) < 5:
            raise serializers.ValidationError("Comment must be at least 5 characters long.")
        return value

    def validate(self, data):
        return data   


class ClientCollectionReadCommmentSerializer(serializers.ModelSerializer):
    """Serializer for reading client collection comments."""

    client = serializers.SlugRelatedField(slug_field='username', read_only=True)
    clientcollection = serializers.SlugRelatedField(slug_field='collection_name', read_only=True)

    class Meta:
        model = ClientCollectionCommment
        
        fields = [
            'id',
            'client', # Client who made the comment
            'clientcollection',
            'comment',
            'comment_date',
        ]
        read_only_fields = fields

class ClientCollectionWriteCommmentSerializer(serializers.ModelSerializer):
    """ Serializer for writing client collection comments."""

    class Meta:
        model = ClientCollectionCommment
        fields = ['clientcollection','comment']

    def validate_comment(self,value):
            if len(value) < 5:
                raise serializers.ValidationError("Comment must be at least 5 characters long.")
            return value

    def validate(self, data):
        request = self.context.get('request')
        client = request.user
        clientcollection = data.get('clientcollection')
        
        if client == clientcollection.client:
            raise serializers.ValidationError(
                "Client cannot comment on their own collection."
            )
        return data
