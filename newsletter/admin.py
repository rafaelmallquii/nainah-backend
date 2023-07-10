from django import forms
from django.contrib import admin
from django_summernote.widgets import SummernoteWidget
from .models import Newsletter, Subscriber
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import re

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
    
    actions = ['send_newsletter']
    
    def send_newsletter(self, request, queryset):
        # send mail to all subscribers with newsletter content as email body and subject as newsletter title
        
        for newsletter in queryset:
            # get all subscribers
            subscribers = Subscriber.objects.all()
            
            # send mail to all subscribers
            for subscriber in subscribers:
                subject = 'Nainah Collection Offert'
                to_email = subscriber.email
                from_email = 'no-reply@nainahcollection.com'
                content = f'{newsletter.content}'
                pattern = r'src="([^"]+)"'
                _host = 'https://nainah.yotohosting.tk'
                content_modified = re.sub(pattern, r'src="{}\\1"'.format(_host), content)
                email = EmailMessage(subject, content_modified, from_email, [to_email])
                email.content_subtype = 'html'
                email.send()
            
            # message success
            self.message_user(request, 'Newsletter sent successfully')
            
    send_newsletter.short_description = 'Send newsletter to all subscribers'

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass