from django.contrib import admin
from .models import Cupon

@admin.register(Cupon)
class DescuentosAdmin (admin.ModelAdmin):
    list_display = (
        'fecha',
        'codigo',
        'descuento_porcentaje',
        'descuento_valor',
        #'mostrar_productos',
    )
    
"""    def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])
    mostrar_productos.short_description = 'Productos'
    
@admin.register(DescuentoProducto)
class DescuentoProductoAdmin (admin.ModelAdmin):
    list_display= (
        'id_descuento',
        'id_producto',
        'fecha_venc',
    )"""