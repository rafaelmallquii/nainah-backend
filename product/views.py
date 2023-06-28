from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, TagSerializer
from .models import Product
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    @extend_schema(
        exclude=True,  # Ignore the 'GET /{id}'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = [
        'name', 
        'description',
        'category__name',
        'tags__name',
        'productvariant__color',
        'productvariant__size',
    ]