import django_filters
from .models import Product
from django_filters import rest_framework as filters

from .models import Tag

class ProductFilter(django_filters.FilterSet):
    enabled = django_filters.BooleanFilter(field_name='enabled')
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags',
        queryset=Tag.objects.all()
    )
    
    category = django_filters.NumberFilter(field_name='category__id')
    trending = django_filters.BooleanFilter(field_name='trending')    
    color = django_filters.CharFilter(field_name='productvariant__color', lookup_expr='icontains')
    size = django_filters.CharFilter(field_name='productvariant__size', lookup_expr='icontains')

    min_price = django_filters.NumberFilter(field_name='productvariant__price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='productvariant__price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []
    
    def filter_tags(self, queryset, name, value):
        tags = value.split(',')
        return queryset.filter(tags__name__in=tags)