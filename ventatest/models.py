from django.db import models

from django.dispatch import receiver

from django.db.models.signals import post_save, pre_save

from core.settings import LANGUAGE_CODE

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Venta(models.Model):

    estado = models.BooleanField(default=False, choices=((True, 'Pagado'), (False, 'Pendiente')))

    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

    cliente_venta = models.CharField(max_length=100)
    productos_venta = models.CharField(max_length=100)


    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.cliente_venta) + ' - ' + str(self.total)
    
    def save(self, *args, **kwargs):
            
        # solo si se esta creando la venta

        if kwargs.get('created', False):

            self.total = 0
            self.cliente_venta = self.clientes.nombre
            self.productos_venta = ''

            for producto in self.productos.all():
                
                self.productos_venta += producto.nombre + ', '
            
            self.total = sum([producto.precio for producto in self.productos.all()])


        super(Venta, self).save(*args, **kwargs)

    class Meta:
        if LANGUAGE_CODE == 'en':
            verbose_name_plural = 'Sales'
            verbose_name = 'Sale'
        else:
            verbose_name_plural = 'Ventas'
            verbose_name = 'Venta'