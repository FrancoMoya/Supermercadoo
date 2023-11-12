from django.db import models
from aplicaciones.producto.models import Producto
from aplicaciones.pedido.models import Pedido

# Relacion entre "Carrito" y "Producto"= MUCHOS A UNO
# Relacion entre "Carrito" y "Pedido"= MUCHOS A UNO
class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=0)
    estado = models.BooleanField ('Estado activo', default=True)
    fecha = models.DateTimeField(auto_now_add=True)
    # Otros campos específicos del detalle del carrito, como precio unitario, subtotal, etc.
    class Meta:
        verbose_name = ('Carrito')
        verbose_name_plural = ('Carritos')
    def __str__(self):
        return f"Pedido: {self.pedido}, Producto: {self.producto}, Cantidad: {self.cantidad}"
    
    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total


"""class Carrito (models.Model):
    id_carritos = models.BigAutoField (primary_key=True)
    customer = models.OneToOneField (Customer, on_delete=models.CASCADE)
    productos = models.ManyToManyField (Producto, through = 'CarritoProducto')
    
class CarritoProducto (models.Model):
    id_carrito = models.ForeignKey (Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey (Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=1)
    estado = models.BooleanField ('Estado activo', default=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.id_producto.precio * self.cantidad
        return total"""
