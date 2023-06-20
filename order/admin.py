from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import Order, OrderItem

from .forms import InlineOrderItemForm

# Register your models here.


class OrderItemInline(admin.TabularInline):
    form = InlineOrderItemForm
    model = OrderItem
    exclude = ['image']
    # raw_id_fields = ['product']
    readonly_fields = ['title', 'image_product', 'price', 'total_price', 'tax',]
    extra = 1

    def image_product(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width ="100px"/>')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # no need to show all products in the dropdown
        
        if db_field.name == 'product':
            kwargs['queryset'] = db_field.related_model.objects.filter(enabled=True)
            
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

        
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [
        OrderItemInline,
    ]
    
    date_hierarchy = 'created'

    list_display = ['name', 'email', 'address', 'city', 'postal_code', 'created', 'updated', 'paid', 'status']
    search_fields = ['paid', 'status']
    list_filter = ['paid', 'status']
    list_per_page = 10
    
    # exclude = ['total',]
    readonly_fields = ['total', 'sub_total',]
    
    # sumarle un USD$ al total
    def sub_total(self, obj):
        if obj.total is not None:
            return mark_safe(f'<b>USD$ {obj.sub_total}</b>')
        return mark_safe(f'<b>USD$ 0.00</b>')
    
    class Media:
        css = {
            'all': ('css/order/order.css',)
        }
        
        js = ('js/order/order.js',)