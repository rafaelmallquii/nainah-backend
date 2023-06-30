from django.db import models
# import valationError
from django.core.exceptions import ValidationError

# Create your models here.

class Setting(models.Model):
    site_name = models.CharField(max_length=100)
    site_banner_small = models.ImageField(upload_to='images/site/')
    site_banner_large = models.ImageField(upload_to='images/site/')
    site_banner_collections = models.ImageField(upload_to='images/site/')
    site_description = models.TextField(max_length=200)
    site_address = models.CharField(max_length=200)
    site_phone = models.CharField(max_length=20)
    site_email = models.CharField(max_length=100)
    site_facebook = models.CharField(max_length=100)
    site_instagram = models.CharField(max_length=100)
    site_tiktok = models.CharField(max_length=100)

    site_icon = models.ImageField(upload_to='images/site/')
    site_logo = models.ImageField(upload_to='images/site/')
    site_favicon = models.ImageField(upload_to='images/site/')

    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        if not self.pk and Setting.objects.exists():
            pass
        else:
            return super(Setting, self).save(*args, **kwargs)

class Currency(models.Model):
    setting = models.OneToOneField(Setting, on_delete=models.CASCADE)
    currency_code = models.CharField(max_length=3, help_text='Enter currency code. Example: USD, EUR, GBP, etc.', blank=True, null=True)
    currency_symbol = models.CharField(max_length=5, help_text='Enter currency symbol. Example: $, €, £, etc.')

    def __str__(self):
        return f'{self.currency_code} {self.currency_symbol}'
    
    class Meta:
        verbose_name_plural = 'Currency'
        

class TaxAndShipment(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, help_text='Enter city name.')
    tax_rate = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        help_text='Enter tax rate e.g. 5.00 for 5% tax.',
        default=0.00
    )
    
    shipment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Enter shipment amount.',
        default=0.00
    )

    def __str__(self):
        return f'{self.city}'

    class Meta:
        verbose_name_plural = 'Tax and Shipment'
        
        
class SiteMeta(models.Model):
    setting = models.OneToOneField(Setting, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=100)
    meta_description = models.TextField(max_length=200)
    meta_keywords = models.TextField()
    meta_author = models.CharField(max_length=100)
    meta_robots = models.CharField(max_length=100)
    meta_image = models.ImageField(upload_to='images/site/')
    
    def __str__(self):
        return f'{self.meta_title}'

    class Meta:
        verbose_name_plural = 'Site Meta'