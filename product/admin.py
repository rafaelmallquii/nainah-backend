from django.contrib import admin
from .models import Product, ProductImage, Tag, MetaAttribute, ProductVariant

from django.utils.safestring import mark_safe
from .forms import ProductForm, InlineProductForm


admin.site.register(Tag)


class MetaAttributeInline(admin.StackedInline):
    model = MetaAttribute
    extra = 1


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['current_image',]


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
        ProductImageInline,
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

    list_display = ['id', 'preview_image', 'title', 'enabled', 'category', ]
    search_fields = ['title',]
    list_filter = ['category', 'enabled', 'trending']

    list_per_page = 10

    # change html of field trending

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
