from rest_framework import serializers
from .models import Catalog
from product.models import Product, ProductVariant

class ProductSerializerParent(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title',)

class ProductCatalogSerializer(serializers.ModelSerializer):
    product = ProductSerializerParent(read_only=True)
    class Meta:
        model = ProductVariant
        fields = (
            # nombre del producto padre
            'product',
            'id',
            'title',
            'image',
            'price',
            'sale_price',
        )

class CatalogSerializer(serializers.ModelSerializer):
    products = ProductCatalogSerializer(many=True, read_only=True)
    class Meta:
        model = Catalog
        fields = '__all__'
        
