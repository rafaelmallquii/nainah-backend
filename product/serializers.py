from rest_framework import serializers
from .models import Product, ProductVariant, MetaAttribute, Tag
from category.serializers import CategorySerializer

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class MetaAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaAttribute
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    variants = ProductVariantSerializer(many=True)
    tags = TagSerializer(many=True)
    meta_attributes = MetaAttributeSerializer(many=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
