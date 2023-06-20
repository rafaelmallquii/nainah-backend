from django.db import models

# Create your models here.

class Coupon(models.Model):
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    min_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Minimum amount to apply coupon')
    discount = models.IntegerField(help_text='Discount in USD')

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code