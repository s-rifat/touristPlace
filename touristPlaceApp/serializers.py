from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Place
        fields = ['id', 'name', 'location', 'country', 'description', 'image', 
        'created_by', 'created_at', 'updated_at']
