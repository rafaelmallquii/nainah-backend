from django.contrib import admin
from .models import Catalog, ProductCatalog

class ProductCatalogInline(admin.TabularInline):
    model = ProductCatalog
    extra = 1

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    inlines = [ProductCatalogInline]