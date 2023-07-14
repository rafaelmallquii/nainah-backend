from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, TagSerializer
from .models import Product, ProductVariant
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

    lookup_field = 'title'  # Campo para buscar por title

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        kwargs[self.lookup_field] = kwargs[lookup_url_kwarg]
        return super().retrieve(request, *args, **kwargs)
    

class AvailableColorsAPIView(APIView):
    @extend_schema(
        description='Get all available colors',
        responses={}        
    )
    def get(self, request):
        colors = ProductVariant.objects.exclude(color__isnull=True).values_list('color', flat=True).distinct()
        return Response(colors)
    
class AvailableSizesAPIView(APIView):
    @extend_schema(
        description='Get all available sizes',
        responses={}
    )
    def get(self, request):
        sizes = ProductVariant.objects.exclude(size__isnull=True).values_list('size', flat=True).distinct()
        return Response(sizes)