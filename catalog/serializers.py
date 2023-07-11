from rest_framework import serializers
from .models import Catalog, ProductCatalog

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'description', 'banner', 'show_quantity', 'created_at', 'updated_at']
        
class ProductCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatalog
        fields = ['id', 'catalog', 'product']