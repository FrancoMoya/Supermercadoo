from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email',
                    'nombre',
                    'apellido',
                    'is_admin']
    list_filter = ['id', 'apellido']
    search_fields = ['nombre']

admin.site.register(User, UserAdmin)