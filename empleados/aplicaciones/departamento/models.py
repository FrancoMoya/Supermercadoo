from django.db import models

# Create your models here.
class Departamento (models.Model):
    nombre = models.CharField('Nombre', max_length=35)    # blank=True (permite vacios) | Max_length ancho  | El 1er valor es la etiqueta
    sigla = models.CharField('Sigla', max_length=10)    # Por defecto NO permite  #El blank si permite o no blancos
    activo = models.BooleanField('¿Está activo?', default= False)     #Un campo boolean  | Si por defecto venia activo o no
    piso = models.PositiveSmallIntegerField('Piso')
    oficina = models.CharField('Oficina N°', max_length=7)
    
    class Meta:
        verbose_name = 'Empresa'    # Para cambiar el nombre de la clase en singular
        verbose_name_plural = ('Departamentos')   # Para cambiar el nombre de la clase en plural
        ordering = ['nombre']  # Se debe poner dentro de las comillas la var del atributo
        unique_together = ('nombre', 'sigla')
    
    def __str__(self):
        return f"{self.nombre} - {self.sigla} - {self.piso} - {self.oficina}"