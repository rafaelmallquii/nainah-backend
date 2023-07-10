from django.contrib import admin
from .models import Product, Tag, MetaAttribute, ProductVariant #  ProductImage,

from django.utils.safestring import mark_safe
from .forms import ProductForm, InlineProductForm


admin.site.register(Tag)
    
class MetaAttributeInline(admin.StackedInline):
    model = MetaAttribute
    extra = 1


# class ProductImageInline(admin.StackedInline):
#     model = ProductImage
#     extra = 1
#     readonly_fields = ['current_image',]


class ProductVariantInline(admin.StackedInline):
    form = InlineProductForm
    model = ProductVariant
    extra = 0

    readonly_fields = ['current_image',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    # list_editable = ['price', 'enabled', ]
    actions_on_bottom = True
    actions_on_top = False
    date_hierarchy = 'created_at'

    # readonly_fields = ('current_image', )

    inlines = [
        ProductVariantInline,
        # ProductImageInline,
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

    readonly_fields = ['current_image',]

    list_display = ['product_id', 'preview_image', 'title', 'enabled', 'category', 'display_price', 'display_stock']

    search_fields = ['title',]
    list_filter = ['category', 'enabled', 'trending']

    list_per_page = 10

    ordering = ('title', 'productvariant__price', 'productvariant__stock')
    
    def display_price(self, obj):
        variant = obj.variants().first()
        if variant:
            return variant.price
        return None

    def display_stock(self, obj):
        variant = obj.variants().first()
        if variant:
            return variant.stock
        return None
    
    display_price.short_description = 'Price'
    display_stock.short_description = 'Stock'

    display_price.admin_order_field = 'productvariant__price'
    display_stock.admin_order_field = 'productvariant__stock'
    

    
    
    
    def trending(self, obj):
        if obj.trending:
            return mark_safe('<span style="color: green;">Yes</span>')
        else:
            return mark_safe('<span style="color: red;">No</span>')

    class Media:
        css = {
            'all': ('css/widgets/checkbox.css',)
        }
        js = ('js/widgets/checkbox.js', 'js/widgets/copyvalues.js')
