from django.contrib import admin
from .models import Catalog# , ProductCatalog
from adminsortable2.admin import SortableAdminMixin

# class ProductCatalogInline(admin.TabularInline):
#     model = ProductCatalog
#     extra = 1

@admin.register(Catalog)
class CatalogAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order', 'name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    # inlines = [ProductCatalogInline]