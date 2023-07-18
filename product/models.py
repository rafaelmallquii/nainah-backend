from django.db import models
from .utils import validator_price
from ckeditor.fields import RichTextField
from category.models import Category
from django.utils.safestring import mark_safe
from setting.models import Color, Size


from .seeds import (
    DEFAULT_DESCRIPTION,
    DEFAULT_TITLE,
    DEFAULT_PRICE,
    DEFAULT_CATEGORY,
)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    enabled = models.BooleanField(default=True, help_text='Is this product Enabled?')
    trending = models.BooleanField(default=False, help_text='Is this product in Trending?')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=DEFAULT_CATEGORY)
    tags = models.ManyToManyField(Tag, blank=True, help_text='Select tags for this product')
    
    title = models.CharField(max_length=100, default=DEFAULT_TITLE, unique=True)
    description = RichTextField(default=DEFAULT_DESCRIPTION)

    image = models.ImageField(upload_to='images/products')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def preview_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width ="100px"/>')
        else:
            return 'No Image'
        
    def current_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="200px" id="image-preview" />')
    
    def product_id(self):
        # Format order id to 4 digits
        return f'#{str(self.pk).zfill(4)}'

    def variants(self):
        return ProductVariant.objects.filter(product=self)
    
    def meta_attributes(self):
        return MetaAttribute.objects.filter(product=self)
    
    product_id.short_description = 'ID'
    product_id.admin_order_field = 'pk'
    

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.PROTECT, blank=True, null=True)
    stock = models.IntegerField(default=1, help_text='Stock of this variant')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[validator_price])
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images/products')

    def current_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="200" id="image-preview" />')

    def __str__(self):
        return f'{self.title} - " - ${self.price}'

class MetaAttribute(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=100, blank=True, null=True)
    meta_keywords = models.CharField(max_length=100, blank=True, null=True)
    meta_image = models.ImageField(upload_to='images/products', blank=True, null=True)

    def __str__(self):
        return self.product.title