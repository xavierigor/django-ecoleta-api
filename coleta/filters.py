from django_filters import rest_framework as filters, Filter

from coleta.models import Point


class MultipleItemsCustomFilter(Filter):

    def filter(self, qs, value):
        if not value:
            return qs

        values = value.split(',')
        for pk in values:
            qs = qs.filter(items__pk=pk)

        return qs


class PointFilter(filters.FilterSet):
    items = MultipleItemsCustomFilter(field_name='items')

    class Meta:
        model = Point
        fields = ['name', 'city', 'uf', 'items']
