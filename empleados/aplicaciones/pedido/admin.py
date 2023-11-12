from django.contrib import admin
from .models import Pedido
class PedidoAdmin (admin.ModelAdmin):
    list_display = (
        'usuario',
        #'total',
        #'medio_de_pago',
        'fecha',
    )
    readonly_fields=['fecha']
admin.site.register(Pedido,PedidoAdmin)
