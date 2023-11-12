from django.db import models
from aplicaciones.usuario.models import User

# Relacion entre "Pedido" y "Usuario"= MUCHOS A UNO (permitir anonimos)
class Pedido (models.Model):
    #TIPOS_PAGOS_CHOICES=(('0','Mercado Pago'),('1','Tarjeta de crédito'),('2','Tarjeta de débito'),)
    #medio_de_pago = models.CharField ('Medio de Pago', max_length=1, choices=TIPOS_PAGOS_CHOICES)
    fecha = models.DateTimeField('Fecha',auto_now_add=True)
    usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    # Otros campos relevantes para el pedido, como estado, dirección de envío, total, etc.
    
    class Meta:
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')
        ordering = ['fecha']
    
    def __str__(self):
        return f"Usuario: {self.usuario}"
        
    """def medio_pago_display(self):
        return dict(self.TIPOS_PAGOS_CHOICES).get(self.medio_de_pago, 'Desconocido')
    ${self.total} - {self.medio_pago_display()}"""
    
    
    """def __str__(self):
        # Formatea la fecha y hora sin microsegundos usando strftime()
        formatted_fecha = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return f"{formatted_fecha}"""
    
    @property
    def get_cart_total(self):
        orderitems = self.carrito_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.carrito_set.all()
        total = sum([item.cantidad for item in orderitems])
        return total
    
"""class Pedido (models.Model):
    id_pedido = models.BigAutoField(primary_key=True)
    fecha_pedido = models.DateTimeField('Fecha',auto_now_add=True)
    customer = models.ForeignKey (Customer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')
        ordering = ['fecha_pedido']
    
    @property
    def get_cart_total(self):
        orderitems = self.carritoproducto_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.carritoproducto_set.all()
        total = sum([item.cantidad for item in orderitems])
        return total"""
