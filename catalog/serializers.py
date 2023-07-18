from rest_framework import serializers
from .models import Catalog
from product.models import Product

class ProductCatalogSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = (
                'title',
                'image',
                
            )

class CatalogSerializer(serializers.ModelSerializer):
    products = ProductCatalogSerializer(many=True, read_only=True)
    class Meta:
        model = Catalog
        fields = '__all__'
        
