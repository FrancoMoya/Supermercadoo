from django.contrib import admin
from .models import Proveedor
# Register your models here.
class ProveedorAdmin (admin.ModelAdmin):
    list_display = (
        'estado',
        'nombre',
        'descripcion',
        'fecha',
    )
    search_fields = ['nombre']
    list_display_links = ('estado',)
admin.site.register(Proveedor,ProveedorAdmin)
