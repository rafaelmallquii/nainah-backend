from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Customer

class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # agregar la clase vTextField en el campo de email
    email.widget.attrs.update({'class': 'vTextField'})


    class Meta:
        model = User
        fields = ("email",)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'vTextField'
        self.fields['password2'].widget.attrs['class'] = 'vTextField'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('city',)
        widgets = {
            'city': forms.TextInput(attrs={'class': 'city-class'}),
        }

        