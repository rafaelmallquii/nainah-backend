from django.db import models
from django_countries.fields import CountryField, Country, CountryDescriptor
from product.models import Product, ProductVariant
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from customer.models import Customer


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

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    
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
    products = models.ManyToManyField(ProductVariant, through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,)
    product = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    
    variant_id = models.CharField(max_length=100, null=True, blank=True)
    # create a custom field to store the price at the moment of the purchase
    title = models.CharField(max_length=200, null=True, blank=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,)

    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.id)


# @receiver([post_save, post_delete], sender=OrderItem)
# def update_order_total(sender, instance, **kwargs):
#     order = instance.order
#     order.total = order.orderitem_set.aggregate(
#         total=models.Sum('total_price'))['total'] or 0.00
#     order.save()


# # Al final del archivo
# post_save.connect(update_order_total, sender=OrderItem)
# post_delete.connect(update_order_total, sender=OrderItem)

# def save(self, *args, **kwargs):
#     if not self.price:
#         self.price = self.product.price

#     if not self.title:
#         self.title = self.product.title

#     if not self.image:
#         self.image = self.product.image

#     self.total_price = self.price * self.quantity

#     self.order.total = self.order.total + self.total_price

#     super().save(*args, **kwargs)