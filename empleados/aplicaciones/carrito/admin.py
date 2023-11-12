from django.contrib import admin
from .models import Carrito

@admin.register(Carrito)
class CarritoAdmin (admin.ModelAdmin):
    list_display = (
        'producto',
        'cantidad',
        'estado',
        'fecha',
        #'mostrar_productos',
    )
    """def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])
    mostrar_productos.short_description = 'Productos'"""
    