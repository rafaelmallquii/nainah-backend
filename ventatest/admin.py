from django.contrib import admin

from .models import Cliente, Producto, Venta

# Register your models here.


admin.site.register(Cliente)
admin.site.register(Producto)


@admin.register(Venta)
class AdminVenta(admin.ModelAdmin):

    list_display = ('cliente_venta', 'productos_venta', 'total', 'estado')

    