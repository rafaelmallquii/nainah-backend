from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'preview_image']
    search_fields = ['name', 'description']
    list_filter = ['name', 'description']
    list_per_page = 10

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="120px" height="120" style="object-fit: cover;" />'.format(url=obj.image.url))