from django import forms
from .models import Stock
from aplicaciones.categoria.models import Categoria
from aplicaciones.producto.models import Producto
from aplicaciones.proveedor.models import Proveedor
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
class ProductoForm(forms.ModelForm):
    categoria_existente = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),  # Aquí estableces el queryset
        required=True,
        label="Categoria"
    )
    class Meta:
        model = Producto
        fields = ['nombre', 'imagen', 'codigo', 'medida', 'tipo_medida', 'descripcion', 'precio', 'descuento_porcentaje', 'descuento_valor', 'categoria_existente']
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
class StockForm(forms.ModelForm):
    producto_existente = forms.ModelChoiceField(
        queryset=Producto.objects.all(),  # Aquí estableces el queryset
        required=True,
        label="Producto"
    )
    proveedor_existente = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),  # Aquí estableces el queryset
        required=True,
        label="Proveedor"
    )
    class Meta:
        model = Stock
        fields = ['producto_existente', 'cantidad', 'fecha_venc', 'numero_lote', 'proveedor_existente']
        # 'precio_compra', 'precio_venta', 'ubicacion', 'descripcion'
    


