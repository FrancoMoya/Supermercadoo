from django.contrib import admin

# Register your models here.
from .models import Categoria
# Register your models here.
class CategoriaAdmin (admin.ModelAdmin):
    list_display = (
        'sigla',
        'nombre',
    )
admin.site.register(Categoria,CategoriaAdmin)