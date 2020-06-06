from coleta.filters import PointFilter
from coleta.models import Point, Item
from rest_framework import viewsets
from coleta.serializers import PointSerializer, ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for /points
    """
    queryset = Point.objects.all().order_by('-created_at')
    serializer_class = PointSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PointFilter


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for /items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
