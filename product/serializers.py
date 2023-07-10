from rest_framework import serializers
from .models import Product, ProductVariant, Tag
from category.serializers import CategorySerializer

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    variants = ProductVariantSerializer(many=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'