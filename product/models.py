from django.db import models
from .utils import validator_price
from ckeditor.fields import RichTextField
from category.models import Category
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    enabled = models.BooleanField(default=False, help_text='Is this product Enabled?')
    trending = models.BooleanField(default=False, help_text='Is this product in Trending?')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    
    name = models.CharField(max_length=100, default='Product Name')
    description = RichTextField(default='Product Description')

    image = models.ImageField(upload_to='images/products', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[validator_price])
    stock = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    stock = models.PositiveBigIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[validator_price])

    image = models.ImageField(upload_to='products', null=True, blank=True)

    def current_image(self):
        return '<img src="%s" width="100px" />' % self.image.url
    
    current_image.allow_tags = True

    def __str__(self):
        return self.product.name

class MetaAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=100)
    meta_value = models.CharField(max_length=100)

    def __str__(self):
        return self.product.name
