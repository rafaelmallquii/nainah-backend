from django.db import models

# Create your models here.

class Coupon(models.Model):
    description = models.CharField(max_length=100, default='Coupon valid for minimum purchases of $', help_text='Coupon description')
    code = models.CharField(max_length=50)
    valid_to = models.DateField(help_text='Coupon valid to')
    min_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Minimum amount to apply coupon ($)')
    value = models.DecimalField(max_digits=5, decimal_places=2, help_text='Discount in Percentage (%)')

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code