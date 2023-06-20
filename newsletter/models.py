from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from setting.models import Setting

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()
    
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def send_email(self):
        if Setting.objects.filter(pk=1).exists():
            subject = Setting.objects.get(pk=1).site_name
            subject = 'Thank you for subscribing to ' + subject
        else:
            subject = 'Thank you for subscribing'
        html_content = render_to_string('email.html', {'email': self.email})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject,
            text_content,
            'noreply@localhost',
            [self.email]
        )

        email.attach_alternative(html_content, 'text/html')
        email.send()

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ['-create_at']


class Subscriber(models.Model):
    email = models.EmailField()
    
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ['-create_at']
