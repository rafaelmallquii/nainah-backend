from django.contrib import admin
from .models import Setting, Currency, TaxAndShipment, SiteMeta, Color, Size
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
    
class InlineColor(admin.TabularInline):
    model = Color
    extra = 1

class InlineSize(admin.TabularInline):
    model = Size
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    
    inlines = [
        InlineCurrency,
        InlineTax,
        InlineSiteMeta,
        InlineColor,
        InlineSize,
    ]
    list_display = ('site_name', 'site_description', 'logo')
    
    @easy.with_tags()
    def logo(self, obj):
        return f'<img src="{obj.site_logo.url}" width="100px">'
