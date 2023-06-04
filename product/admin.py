from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Tag, ProductImage, MetaAttribute, ProductVariant

from .forms import ProductForm

# Register your models here.

admin.site.register(Tag)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

    readonly_fields = ['show_image']

    def show_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" />'.format(url=obj.image.url))


class MetaAttributeInline(admin.TabularInline):
    model = MetaAttribute
    extra = 1


class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    form = ProductForm

    actions_on_bottom = True
    actions_on_top = False

    date_hierarchy = 'created_at'

    readonly_fields = ('current_image', )

    inlines = [
        ProductImageInline,
        ProductVariantInline,
        MetaAttributeInline,
    ]

    # add action
    actions = ['unmake_trending', 'make_trending']

    def make_trending(self, request, queryset):
        queryset.update(trending=True)

    def unmake_trending(self, request, queryset):
        queryset.update(trending=False)

    make_trending.short_description = "Mark selected products as trending"
    unmake_trending.short_description = "Unmark all products as trending"

    list_display = ['name', 'price', 'show_image', 'category', 'enabled']
    search_fields = ['name', 'price']
    list_filter = ['price', 'category', 'enabled', 'trending']

    list_per_page = 10

    # cambiar label de la columna

    def show_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" />'.format(url=obj.image.url))

    def current_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" />'.format(url=obj.image.url))

    # cambiar el html del campo trending
    def trending(self, obj):
        if obj.trending:
            return mark_safe('<span style="color: green;">Yes</span>')
        else:
            return mark_safe('<span style="color: red;">No</span>')

    class Media:
        css = {
            'all': ('css/widgets/checkbox.css',)
        }
        js = ('js/widgets/checkbox.js',)