from django.contrib import admin
from .models import Setting, Tax, ShippingCharge, SiteMeta

class InlineSiteMeta(admin.StackedInline):
    model = SiteMeta
    extra = 1

class InlineTax(admin.StackedInline):
    model = Tax
    extra = 1
    
class InlineShippingCharge(admin.StackedInline):
    model = ShippingCharge
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    inlines = [
        InlineTax,
        InlineShippingCharge,
        InlineSiteMeta,
    ]
    list_display = ('site_name', 'site_description', 'site_logo')