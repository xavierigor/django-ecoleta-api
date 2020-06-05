from coleta.models import Point, Item
from rest_framework import viewsets
from coleta.serializers import PointSerializer, ItemSerializer


class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Point.objects.all().order_by('-created_at')
    serializer_class = PointSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
