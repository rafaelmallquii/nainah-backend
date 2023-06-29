from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Order, OrderItem
from .forms import InlineOrderItemForm
from .utils import generate_pdf
from setting.models import Currency


class OrderItemInline(admin.TabularInline):
    form = InlineOrderItemForm
    model = OrderItem
    exclude = ['image']
    # raw_id_fields = ['product']
    readonly_fields = ['title', 'variant_id', 'image_product', 'price', 'total_price', 'tax',]
    extra = 1

    def image_product(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width ="100px"/>')

    
        
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [
        OrderItemInline,
    ]
    
    date_hierarchy = 'created'

    list_display = ['order_id', 'customer', 'paid', 'status', '_sub_total', 'tax', 'shipping_charge', 'total', 'created', 'updated',]
    search_fields = ['paid', 'status']
    list_filter = ['paid', 'status']
    list_per_page = 10
    
    # exclude = ['total',]
    readonly_fields = ['sub_total', 'tax', 'shipping_charge','total',]
    
    # sumarle un USD$ al total
    def _sub_total(self, obj):
        currency = Currency.objects.first()

        if obj.total is not None:
            return mark_safe(f'<b> {currency.currency_symbol} {obj.sub_total}</b>')
        return mark_safe(f'<b>{currency.currency_symbol} 0.00</b>')
    
    class Media:
        css = {
            'all': ('css/order/order.css',)
        }
        
        js = ('js/order/order.js',)
        
    actions = ['export_as_pdf']

    def export_as_pdf(self, request, queryset):
        for order in queryset:
            pdf_response = generate_pdf(order)
            return pdf_response

    export_as_pdf.short_description = "Export selected orders as PDF"