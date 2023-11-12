from django.db import models

class CategoriaTransaccion(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name = ('Categoria Financiera')
        verbose_name_plural = ('Categorias Financieras')
        ordering = ['nombre']
    def __str__(self):
        return f"Nombre: {self.nombre}"

class TransaccionFinanciera(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now_add=True)
    categoria = models.ForeignKey(CategoriaTransaccion, on_delete=models.CASCADE)
    monto = models.DecimalField('Monto',max_digits=10, decimal_places=2)
    descripcion = models.TextField('Descripción')
    class Meta:
        verbose_name = ('Finanzas')
        verbose_name_plural = ('Reportes de Finanzas')
        ordering = ['fecha']
    def __str__(self):
        return f"Categoria: {self.categoria}, Monto: {self.monto}"
