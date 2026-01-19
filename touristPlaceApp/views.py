from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Place
from .serializers import PlaceSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

