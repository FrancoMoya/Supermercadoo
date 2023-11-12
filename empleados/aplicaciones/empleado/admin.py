from django.contrib import admin
from .models import Empleado

# Register your models here.

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',        # Para poder listar los datos que quiero en tabla
        'trabajo',
        'departamento',
    )
admin.site.register(Empleado, EmpleadoAdmin)