from django.db import models
from django_countries.fields import CountryField, Country, CountryDescriptor
from product.models import Product, ProductVariant
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from customer.models import Customer
from setting.models import TaxAndShipment
from .utils import calculate_tax
from coupon.models import Coupon
from django.db.models import F

ORDER_STATUS_CHOICES = (
    ('P', 'Pending'),
    ('PR', 'Processing'),
    ('S', 'Shipped'),
    ('D', 'Delivered'),
    ('R', 'Refounded'),
    ('C', 'Canceled'),
)

class Order(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, default='', blank=True)
    city = models.ForeignKey(TaxAndShipment, on_delete=models.PROTECT, help_text='Select City.')
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='United States of America')
    note = models.TextField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    
    delivery_option = models.CharField(
        max_length=20,
        choices=(
            ('shipping', 'Shipping'),
            ('store_pickup', 'Store Pickup'),
            ('delivery', 'Delivery'),
        ),
        default='shipping'
    )
    
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default='P')
    products = models.ManyToManyField(ProductVariant, through='OrderItem', default=0.00)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    shipping_charge = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # ip_address_client = models.GenericIPAddressField(null=True, blank=True)
    
    def calculate_coupon_discount(self):
        if self.coupon:
            self.discount = float(self.sub_total) * float((self.coupon.value / 100))
        else:
            self.discount = 0
    
    def calculate_shipping(self):
        if self.delivery_option == 'shipping':
            self.shipping_charge = self.city.shipment_amount
        if self.delivery_option == 'store_pickup':
            self.shipping_charge = 0
        if self.shipping_charge == 'delivery':
            self.shipping_charge = 0
    
    def calculcate_orderitem_total(self):
        try:
            if self.orderitem_set.all().count() > 0:
                self.total = self.sub_total + self.tax + self.shipping_charge - self.discount
        except:
            pass
    
    def save(self, *args, **kwargs):
        
        self.calculate_shipping()
        self.calculate_coupon_discount()
        self.calculcate_orderitem_total()
        super().save(*args, **kwargs)
    
    def order_id(self):
        # Format order id to 4 digits
        return f"#{str(self.pk).zfill(4)}"
    
    order_id.short_description = 'ID'
    order_id.admin_order_field = 'pk'
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order:#{str(self.pk).zfill(4)} - ${self.total}'
    

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
            self.tax = calculate_tax(self.order.city.tax_rate, self.total_price)
            
        super().save(*args, **kwargs)


@receiver([post_save, post_delete], sender=OrderItem)
def update_order_total(sender, instance, **kwargs):
    order = instance.order
    order.sub_total = order.orderitem_set.aggregate(total=models.Sum('total_price'))['total'] or 0.00
    order.tax = order.orderitem_set.aggregate(tax=models.Sum('tax'))['tax'] or 0.00
    order.total = float(order.sub_total) + float(order.tax) + float(order.shipping_charge) - float(order.discount)
    
    order.save()

post_save.connect(update_order_total, sender=OrderItem)
post_delete.connect(update_order_total, sender=OrderItem)


@receiver(pre_save, sender=Order)
def check_variable_change(sender, instance, **kwargs):
    if instance.pk:
        saved_instance = Order.objects.get(pk=instance.pk)
        if not saved_instance.paid and instance.paid:
            print('Reduce stock')
            # Deduct stock from product variant
            for item in instance.orderitem_set.all():
                product_variant = item.product
                product_variant.stock -= item.quantity
                product_variant.save()
        elif saved_instance.paid and not instance.paid:
            print('Add stock')
            # Add stock to product variant
            for item in instance.orderitem_set.all():
                product_variant = item.product
                product_variant.stock += item.quantity
                product_variant.save()