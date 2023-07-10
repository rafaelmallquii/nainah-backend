from django.contrib import admin
from .models import Product, Tag, MetaAttribute, ProductVariant #  ProductImage,
from django.utils.safestring import mark_safe
from .forms import ProductForm, InlineProductForm
from django.db.models import Q
import easy

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
    change_list_template = 'admin/product/change_list.html'
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

    list_display = ['product_id', 'preview_image', 'title',  'display_price', 'display_stock', 'enabled', 'category']

    search_fields = ['title', 'id']
    list_filter = ['category', 'enabled', 'trending']

    list_per_page = 10

    # ordering = ('title', 'productvariant__price', 'productvariant__stock')
    
    @easy.with_tags()
    def display_price(self, obj):
        variant = obj.variants().first()
        if variant:
            return f'<b><a>${variant.price}</a></b>'
        return None

    @easy.with_tags()
    def display_stock(self, obj):
        variant = obj.variants().first()
        if variant:
            return f'<b><a>{variant.stock}</a></b>'
        return None
    
    display_price.short_description = 'Price'
    display_stock.short_description = 'Stock'

    display_price.admin_order_field = 'productvariant__price'
    display_stock.admin_order_field = 'productvariant__stock'
    

    def get_search_results(self, request, queryset, search_term):
        use_distinct = False
        if search_term.isnumeric():
            search_value = int(search_term)
            queryset = queryset.filter(Q(id=search_value) | Q(id=search_value))
        else:
            queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct
    
    
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
