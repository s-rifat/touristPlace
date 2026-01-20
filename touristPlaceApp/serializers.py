from rest_framework import serializers
from .models import Place, PlaceImage, Country
import os

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'image', 'uploaded_at']

class PlaceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    images = PlaceImageSerializer(many=True, read_only=True)
    new_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    remove_image_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )
    delete_all_images = serializers.BooleanField(write_only=True, required=False, default=False)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'location', 'country', 'description',
            'images', 'new_images', 'remove_image_ids', 'delete_all_images',
            'created_by', 'created_at', 'updated_at'
        ]

    def update(self, instance, validated_data):
        # Remove specific images
        remove_ids = validated_data.pop('remove_image_ids', [])
        PlaceImage.objects.filter(id__in=remove_ids, place=instance).delete()

        # Remove all images if flagged
        if validated_data.pop('delete_all_images', False):
            instance.images.all().delete()

        # Add new images
        new_images = validated_data.pop('new_images', [])
        for img in new_images:
            PlaceImage.objects.create(place=instance, image=img)

        return super().update(instance, validated_data)

    def create(self, validated_data):
        new_images = validated_data.pop('new_images', [])
        validated_data.pop('delete_all_images', None)
        validated_data.pop('remove_image_ids', None)
        place = super().create(validated_data)
        for img in new_images:
            PlaceImage.objects.create(place=place, image=img)
        return place

