from coleta.models import Point, Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image')

    class Meta:
        model = Item
        fields = ['id', 'title', 'image_url']


class ItemPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title']


class PointSerializer(serializers.ModelSerializer):
    items = ItemPointSerializer(read_only=True, many=True)

    class Meta:
        model = Point
        fields = '__all__'
