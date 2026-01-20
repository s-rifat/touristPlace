from django.contrib import admin

# Register your models here.
from .models import Place, PlaceImage, Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'country', 'created_by', 'created_at']

@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'image', 'uploaded_at']