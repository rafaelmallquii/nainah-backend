from django import forms
from django.contrib import admin
from django_summernote.widgets import SummernoteWidget
from .models import Newsletter, Subscriber
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .utils import agregar_host

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
    list_display = ['subject']
    actions = ['send_newsletter']
    
    def send_newsletter(self, request, queryset):
        # send mail to all subscribers with newsletter content as email body and subject as newsletter title
        for newsletter in queryset:
            # get all subscribers
            subscribers = Subscriber.objects.all()
            
            # send mail to all subscribers
        to_emails = [subscriber.email for subscriber in subscribers]
        subject = newsletter.subject        
        from_email = 'no-reply@nainahcollection.com'
        content = f'{newsletter.content}'
        new_content = agregar_host(content, settings.HOST_NAME)
        email = EmailMessage(subject, new_content, from_email, to_emails)
        email.content_subtype = 'html'
        email.send()
                
        # message success
        self.message_user(request, 'Newsletter sent successfully')
            
    send_newsletter.short_description = 'Send newsletter to all subscribers'

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass