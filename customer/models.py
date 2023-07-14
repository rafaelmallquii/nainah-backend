from django.db import models
from django.contrib.auth.models import AbstractUser
from setting.models import TaxAndShipment

class Customer(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField('Email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    phone = models.CharField(max_length=20, blank=True, null=True)
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, default='United States of America', blank=True, null=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    
class Whishlist(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)