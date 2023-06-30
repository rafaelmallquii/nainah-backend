from django.contrib import admin
from .models import Setting, Currency, TaxAndShipment, SiteMeta
import easy

class InlineSiteMeta(admin.StackedInline):
    model = SiteMeta
    extra = 1

class InlineTax(admin.TabularInline):
    model = TaxAndShipment
    extra = 1
    
class InlineCurrency(admin.StackedInline):
    model = Currency
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    
    inlines = [
        InlineCurrency,
        InlineTax,
        InlineSiteMeta,
    ]
    list_display = ('site_name', 'site_description', 'logo')
    
    @easy.with_tags()
    def logo(self, obj):
        return f'<img src="{obj.site_logo.url}" width="100px">'
