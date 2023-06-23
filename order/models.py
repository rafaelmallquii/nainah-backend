from django.db import models
from django_countries.fields import CountryField, Country, CountryDescriptor
from product.models import Product, ProductVariant
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from customer.models import Customer
from setting.models import Tax, ShippingCharge


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
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='US')
    paid = models.BooleanField(default=False)
    
    delivery_option = models.CharField(
        max_length=20,
        choices=(
            ('delivery', 'Delivery'),
            ('store_pickup', 'Store Pickup')
        ),
        default='delivery'
    )
    
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default=PENDING)
    products = models.ManyToManyField(ProductVariant, through='OrderItem', default=0.00)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_charge = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.delivery_option == 'delivery':
            self.shipping_charge = ShippingCharge.objects.first().amount
        if self.delivery_option == 'store_pickup':
            self.shipping_charge = 0
        if self.shipping_charge == 'free':
            self.shipping_charge = 0
            
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,)
    product = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    variant_id = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if self.product:
            self.variant_id = self.product.id
            self.title = self.product.title
            self.price = self.product.price
            self.image = self.product.image
            self.total_price = self.price * self.quantity
            self.tax = self.total_price * Tax.objects.first().tax_percentage
            
        super().save(*args, **kwargs)


@receiver([post_save, post_delete], sender=OrderItem)
def update_order_total(sender, instance, **kwargs):
    order = instance.order
    order.sub_total = order.orderitem_set.aggregate(
        total=models.Sum('total_price'))['total'] or 0.00
    
    order.tax = order.orderitem_set.aggregate(
        tax=models.Sum('tax'))['tax'] or 0.00
    
    order.total = order.sub_total + order.tax + order.shipping_charge
    
    order.save()



post_save.connect(update_order_total, sender=OrderItem)
post_delete.connect(update_order_total, sender=OrderItem)
