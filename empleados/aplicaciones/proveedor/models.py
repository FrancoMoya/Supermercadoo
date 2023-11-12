from django.db import models

# Create your models here.
class Proveedor (models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    telefono = models.PositiveIntegerField('Teléfono')
    direccion = models.CharField('Dirección', max_length=50)
    mail = models.EmailField('Correo electrónico')
    sitio_web = models.URLField('Sitio Web')
    descripcion = models.TextField('Descripción')
    estado = models.BooleanField('Estado activo')
    fecha = models.DateField('Fecha de creación')
    notas = models.TextField('Notas')
    class Meta:
        verbose_name = ('Proveedor')
        verbose_name_plural = ('Proveedores')
        ordering = ['-fecha']
        
    def __str__(self):
        return f"{self.nombre}"