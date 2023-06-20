from django.db import models

from django_countries.fields import CountryField, Country, CountryDescriptor

from product.models import Product

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

    country = models.CharField(max_length=100, default='US')
    
    delivery_option = models.CharField(
        max_length=20,
        choices=(
            ('delivery', 'Delivery'),
            ('store_pickup', 'Store Pickup')
        ),
        default='delivery'
    )

    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default=PENDING)

    products = models.ManyToManyField(Product, through='OrderItem')
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Order {self.id} Item {self.product}'

    def get_cost(self):
        return self.price * self.quantity
    