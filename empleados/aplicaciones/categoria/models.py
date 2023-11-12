from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField('Nombre', max_length=30,)    # blank=True (permite vacios) | Max_length ancho  | El 1er valor es la etiqueta
    sigla = models.CharField('Sigla', max_length=10,)    # Por defecto NO permite  #El blank si permite o no blancos
    # default='ValorPredeterminado' (hace que inicie con ese valor)
    class Meta:
        verbose_name = 'Categoria'    # Para cambiar el nombre de la clase en singular
        verbose_name_plural = ('Categorias')   # Para cambiar el nombre de la clase en plural
        ordering = ['nombre']  # Se debe poner dentro de las comillas la var del atributo
        unique_together = ('nombre', 'sigla')
    
    def __str__(self):
        return self.sigla+' - '+self.nombre