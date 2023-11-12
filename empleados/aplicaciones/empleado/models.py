from django.db import models
from aplicaciones.departamento.models import Departamento # Importo departamento

class Empleado (models.Model):
    #Modelo de empleado
    JOB_CHOICES =(
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Analista Funcional'),
        ('4', 'Otro'),
    )
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    trabajo = models.CharField('Puesto', max_length=1, choices=JOB_CHOICES)
    sueldo = models.PositiveBigIntegerField('Sueldo')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Relacion entre departamento y empleado (De 1 a muchos)
    class Meta:
        verbose_name = ('Mi empleado')
        verbose_name_plural = ('Empleados de la empresa')
        ordering = ['nombre',]
        unique_together = ('nombre', 'departamento')
    
    def __str__(self):
        return self.nombre+' - '+self.apellido