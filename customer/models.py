from django.db import models

# foreign key to user model
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    username = models.CharField(max_length=50, unique=True)

    email = models.EmailField('Email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # add additional fields in here
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    # add css class to the field
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    # add additional fields in here
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'Customers'
        verbose_name = 'Customer'
    
class Whishlist(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)