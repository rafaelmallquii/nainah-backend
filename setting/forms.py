from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import (
    AboutUs,
    PrivacyPolicy,
    ShippingPolicy,
    TermsAndConditions,
    ReturnsAndRefundsPolicy,
)

class AboutUsAdminForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'label': ''}),
        }
        
class PrivacyPolicyAdminForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'label': ''}),
        }
        
class ShippingPolicyAdminForm(forms.ModelForm):
    class Meta:
        model = ShippingPolicy
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'label': ''}),
        }
        
class TermsAndConditionsAdminForm(forms.ModelForm):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'label': ''}),
        }
        
class ReturnsAndRefundsPolicyAdminForm(forms.ModelForm):
    class Meta:
        model = ReturnsAndRefundsPolicy
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'label': ''}),
        }