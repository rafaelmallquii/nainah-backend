from django import forms
from django.contrib import admin
from django_summernote.widgets import SummernoteWidget

from .models import Newsletter, Subscriber

class NewsletterAdminForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'label': ''}),
        }

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    form = NewsletterAdminForm



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass