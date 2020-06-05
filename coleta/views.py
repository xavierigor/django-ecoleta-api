from coleta.models import Point, Item
from rest_framework import viewsets
from coleta.serializers import PointSerializer, ItemSerializer


class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for /points
    """
    queryset = Point.objects.all().order_by('-created_at')
    serializer_class = PointSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for /items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
