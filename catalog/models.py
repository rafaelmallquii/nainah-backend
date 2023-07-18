from django.db import models
from product.models import Product, ProductVariant

# Create your models here.

class Catalog(models.Model):
    active = models.BooleanField(default=True, help_text='Is this catalog active?')
    name = models.CharField(max_length=100, default='New Collection', help_text='Name of the catalog')
    description = models.TextField()
    banner = models.ImageField(upload_to='catalog/banner', blank=True, null=True)
    show_quantity = models.PositiveIntegerField(default=8, choices=((4,4),(8,8)), help_text='Show quantity of products in catalog?')
    products = models.ManyToManyField(ProductVariant, blank=True, related_name='catalog_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    
    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'
        ordering = ['order']