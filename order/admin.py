from django.contrib import admin

from .models import Order, OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
    
    extra = 1

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