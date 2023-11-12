from django.shortcuts import render
from .models import Categoria
from aplicaciones.producto.models import Producto
def categorias (request, nombre_categoria):
    categoria = Categoria.objects.get(nombre=nombre_categoria)
    productos = Producto.objects.filter(categoria=categoria)
    
    return render(request, 'categoria/categoria.html', {
        'categoria': categoria, 'productos': productos
    })