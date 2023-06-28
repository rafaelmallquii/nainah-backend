from django import forms

from .models import Order, OrderItem

class InlineOrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
        widgets = {
            'quantity': forms.NumberInput(attrs={'style': 'width: 70px;'}),
        }