from django.contrib import admin
from .models import Setting, Currency, TaxAndShipment, SiteMeta, Color, Size
import easy
from django_summernote.widgets import SummernoteWidget

from .models import (
    AboutUs,
    PrivacyPolicy,
    ShippingPolicy,
    TermsAndConditions,
    ReturnsAndRefundsPolicy,
)

from .forms import (
    AboutUsAdminForm,
    PrivacyPolicyAdminForm,
    ShippingPolicyAdminForm,
    TermsAndConditionsAdminForm,
    ReturnsAndRefundsPolicyAdminForm,
)

class InlineAboutUs(admin.StackedInline):
    model = AboutUs
    extra = 1
    form = AboutUsAdminForm
    
class InlinePrivacyPolicy(admin.StackedInline):
    model = PrivacyPolicy
    extra = 1
    form = PrivacyPolicyAdminForm
    
class InlineShippingPolicy(admin.StackedInline):
    model = ShippingPolicy
    extra = 1
    form = ShippingPolicyAdminForm
    
class InlineTermsAndConditions(admin.StackedInline):
    model = TermsAndConditions
    extra = 1
    form = TermsAndConditionsAdminForm

class InlineReturnsAndRefundsPolicy(admin.StackedInline):
    model = ReturnsAndRefundsPolicy
    extra = 1
    form = ReturnsAndRefundsPolicyAdminForm

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
        InlineAboutUs,
        InlinePrivacyPolicy,
        InlineShippingPolicy,
        InlineTermsAndConditions,
        InlineReturnsAndRefundsPolicy,
    ]
    list_display = ('site_name', 'site_description', 'logo')
    
    @easy.with_tags()
    def logo(self, obj):
        return f'<img src="{obj.site_logo.url}" width="100px">'
