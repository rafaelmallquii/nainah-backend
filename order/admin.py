from django.contrib import admin

from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'

    list_display = ['name', 'email', 'address', 'city', 'postal_code', 'created', 'updated', 'paid', 'status']
    search_fields = ['paid', 'status']
    list_filter = ['paid', 'status']
    list_per_page = 10