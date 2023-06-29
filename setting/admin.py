from django.contrib import admin
from .models import Setting, Currency, Tax, ShippingCharge, SiteMeta

class InlineSiteMeta(admin.StackedInline):
    model = SiteMeta
    extra = 1

class InlineTax(admin.StackedInline):
    model = Tax
    extra = 1
    
class InlineShippingCharge(admin.StackedInline):
    model = ShippingCharge
    extra = 1

class InlineCurrency(admin.StackedInline):
    model = Currency
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    inlines = [
        InlineCurrency,
        InlineTax,
        InlineShippingCharge,
        InlineSiteMeta,
    ]
    list_display = ('site_name', 'site_description', 'site_logo')