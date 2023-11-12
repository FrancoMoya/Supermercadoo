from django.contrib import admin
from .models import Stock
# Register your models here.

class StockAdmin (admin.ModelAdmin):
    list_display = (
        'producto',
        'cantidad',
        'fecha_venc',
        'numero_lote',
        'proveedor',
    )
    search_fields = ['producto']
    list_filter =['producto']
    
admin.site.register(Stock, StockAdmin)
