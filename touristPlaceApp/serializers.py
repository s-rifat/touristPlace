from rest_framework import serializers
from .models import Place
import os

class PlaceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    image = serializers.ImageField(required=False)
    remove_image = serializers.BooleanField(write_only=True, required=False, default=False)


    class Meta:
        model = Place
        fields = ['id', 'name', 'location', 'country', 'description', 'image', 
        'remove_image', 'created_by', 'created_at', 'updated_at']
    
    def update(self, instance, validated_data):
        # Check if remove_image is True
        if validated_data.pop('remove_image', False):
            # Delete the old file
            if instance.image and os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
            instance.image = None

        # Update the image if a new file is provided
        if 'image' in validated_data:
            # Delete old image if it exists
            if instance.image and os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
            instance.image = validated_data.get('image', instance.image)

        return super().update(instance, validated_data)

