from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, PlaceViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'countries', CountryViewSet, basename='country')


urlpatterns = [
    path('', include(router.urls)),
]
