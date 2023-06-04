from django.db import models

from django_countries.fields import CountryField, Country, CountryDescriptor

# Create your models here.

class Order(models.Model):

    PENDING = 'P'
    PROCESSING = 'PR'
    SHIPPED = 'S'
    DELIVERED = 'D'
    REFOUNDED = 'R'
    CANCELED = 'C'

    ORDER_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (REFOUNDED, 'Refounded'),
        (CANCELED, 'Canceled'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    pais = CountryField(multiple=True)
    
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default=PENDING)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Order {self.id} Item {self.product}'
    
    def get_cost(self):
        return self.price * self.quantity
    