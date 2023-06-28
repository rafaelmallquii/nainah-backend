from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    http_method_names = ['get',]
    
    @extend_schema(
        exclude=True,  # Ignore the 'GET /{id}'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)