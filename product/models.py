from django.db import models
from .utils import validator_price
from ckeditor.fields import RichTextField
from category.models import Category
from django.utils.safestring import mark_safe

from .choices import (
    SIZE_CHOICES,
    COLOR_CHOICES
)

from .seeds import (
    DEFAULT_DESCRIPTION,
    DEFAULT_TITLE,
    DEFAULT_PRICE,
    DEFAULT_CATEGORY,
)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    enabled = models.BooleanField(default=False, help_text='Is this product Enabled?')
    trending = models.BooleanField(default=False, help_text='Is this product in Trending?')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=DEFAULT_CATEGORY)
    tags = models.ManyToManyField(Tag, blank=True)
    
    title = models.CharField(max_length=100, default=DEFAULT_TITLE)
    description = RichTextField(default=DEFAULT_DESCRIPTION)

    color = models.CharField(max_length=100, choices=COLOR_CHOICES, blank=True, null=True)

    size = models.CharField(max_length=100, choices=SIZE_CHOICES, blank=True, null=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=DEFAULT_PRICE, validators=[validator_price])
    offert_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, validators=[validator_price])
    stock = models.PositiveBigIntegerField(default=0)

    image = models.ImageField(upload_to='images/products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - ${self.price}'
    
    def preview_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width ="100px"/>')
        else:
            return 'No Image'
        
    def current_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="200px" id="image-preview" />')


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    color = models.CharField(max_length=100,choices=COLOR_CHOICES, blank=True, null=True)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES, blank=True, null=True)
    
    stock = models.PositiveBigIntegerField(default=0, help_text='Stock of this variant')
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[validator_price])
    image = models.ImageField(upload_to='images/products')

    def current_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="200" id="image-preview" />')
    
    # current_image.allow_tags = True

    def __str__(self):
        return f'{self.title} - $ {self.price}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products')

    def __str__(self):
        return self.product.title
    
    def current_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="200" id="" />')

class MetaAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=100)
    meta_value = models.CharField(max_length=100)

    def __str__(self):
        return self.product.title
