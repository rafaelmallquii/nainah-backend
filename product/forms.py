from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'enabled': forms.CheckboxInput(attrs={'class': 'my-checkbox-enabled'}),
            'trending': forms.CheckboxInput(attrs={'class': 'my-checkbox'}),
            
        }

class InlineProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'my-title-input'}),
        }