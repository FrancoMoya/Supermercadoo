from django.db import models
from aplicaciones.categoria.models import Categoria
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

def validate_two_digit(value):
    if not (0 <= value <= 99):
        raise ValidationError("El porcentaje debe ser un número de dos dígitos (0-99).")
class Producto (models.Model):
    #Modelo de producto
    MEDIDAS_CHOICES =(
        ('0', 'Grs'),
        ('1', 'Kgs'),
        ('2', 'Cm3'),
        ('3', 'Mls'),
        ('4', 'Lts'),
    )
    nombre = models.CharField('Nombre', max_length=50)
    imagen = models.ImageField('Imagen', null=True, blank=True)
    codigo = models.CharField('Código', max_length=50)
    medida = models.DecimalField('Medida', max_digits=6, decimal_places=2)
    tipo_medida = models.CharField('Tipo de medida', max_length=1, choices=MEDIDAS_CHOICES)
    descripcion = models.TextField('Descripción')  # Campo de texto largo
    precio = models.DecimalField('Precio ($)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Campo decimal (10 digitos incluyendo dec)(2 decimales)
    #Para poder agregar un descuento a un producto en especifico
    descuento_porcentaje = models.IntegerField('Porcentaje de descuento', validators=[validate_two_digit], null=True, blank=True)
    descuento_valor = models.IntegerField('Valor de descuento', null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)
    # Relacion entre producto y categoria (De muchos a muchos)
    def total_stock(self):
        total = sum(stock.cantidad for stock in self.stock_set.all())  # Itera por cada producto relacionado a su stock,cantidad y lo suma
        return total
    total_stock.short_description = "Total de Stock"  # Para elegir el nombre personalizado desde la vista del administrador de stock
    
    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')
        ordering = ['nombre']
        unique_together = ('nombre', 'codigo', 'tipo_medida', 'medida')
    def get_tipo_medida_display(self):
        return dict(Producto.MEDIDAS_CHOICES)[self.tipo_medida]
    def __str__(self):
        tipo_medida = self.get_tipo_medida_display()
        return f"{self.nombre} - {self.medida} {tipo_medida}"
    #Para que acceda a la imagen como un atributo y no como un metodo
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url
