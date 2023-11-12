from django.contrib import admin
from .models import Producto
# Register your models here.
class ProductoAdmin (admin.ModelAdmin):
    list_display = (
        'codigo',
        'categorias_display',
        'nombre',
        'medida',
        'tipo_medida',    # Para poder listar los datos que quiero en tabla
        'precio',
        'total_stock',
    )
    
    def categorias_display (self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categoria.all()])
    categorias_display.short_description = 'Categorías'
    search_fields = ['nombre','codigo']
    list_filter = ['categoria']
    list_editable = ['precio']
admin.site.register(Producto,ProductoAdmin)
