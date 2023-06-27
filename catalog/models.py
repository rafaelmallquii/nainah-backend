from django.db import models
from product.models import Product

# Create your models here.

class Catalog(models.Model):
    active = models.BooleanField(default=True, help_text='Is this catalog active?')
    name = models.CharField(max_length=100, default='New Collection', help_text='Name of the catalog')
    description = models.TextField()
    banner = models.ImageField(upload_to='catalog/banner', blank=True, null=True)
    show_quantity = models.PositiveIntegerField(default=8, choices=((4,4),(8,8)), help_text='Show quantity of products in catalog?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'
        ordering = ['-created_at']
        
class ProductCatalog(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.catalog.name} - {self.product.title}'

    class Meta:
        verbose_name = 'Product Catalog'
        verbose_name_plural = 'Product Catalogs'
        ordering = ['-catalog']