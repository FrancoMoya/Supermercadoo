from django.contrib import admin
from .models import TransaccionFinanciera

@admin.register(TransaccionFinanciera)
class TransaccionFinancieraAdmin (admin.ModelAdmin):    
    list_display = (
        'descripcion',
        'fecha',
    )
    
    readonly_fields=['fecha']