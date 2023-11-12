from django.shortcuts import render, redirect, get_object_or_404
from .forms import StockForm, ProductoForm, ProveedorForm, CategoriaForm
from aplicaciones.producto.models import Producto
from aplicaciones.categoria.models import Categoria
from aplicaciones.proveedor.models import Proveedor
from .models import Stock
from django.views.generic.edit import CreateView
from django.urls import reverse

class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/agregar_stock.html'

    def form_valid(self, form):
        producto_existente = form.cleaned_data.get('producto_existente')
        proveedor_existente = form.cleaned_data.get('proveedor_existente')

        producto = Producto.objects.get(pk=producto_existente.pk)
        proveedor = Proveedor.objects.get(pk=proveedor_existente.pk)

        form.instance.producto = producto
        form.instance.proveedor = proveedor

        return super().form_valid(form)
    def get_success_url(self):
        return reverse('home')



def stock_create_from_producto(request, producto_id=None):
    if producto_id:
        producto = Producto.objects.get(pk=producto_id)
        form = StockForm(initial = {'producto_existente': producto})
    else:
        form = StockForm()

    return render(request, 'stock/agregar_stock.html', {'form': form})

def stock_create_from_proveedor(request, proveedor_id=None):
    if proveedor_id:
        proveedor = Proveedor.objects.get(pk=proveedor_id)
        form = StockForm(request.POST or None, initial={'proveedor_existente': proveedor})

        if request.method == 'POST':
            producto_id = request.POST.get('producto')  # Asegúrate de que el nombre del campo sea correcto
            producto = Producto.objects.get(pk=producto_id)
            form = StockForm(request.POST)

            if form.is_valid():
                stock_instance = form.save(commit=False)
                stock_instance.proveedor = proveedor
                stock_instance.producto = producto
                stock_instance.save()
                return redirect('stock_create')

    else:
        form = StockForm()

    return render(request, 'stock/agregar_stock.html', {'form': form})

def producto_create_from_categoria(request, categoria_id=None):
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            producto.categoria.add(categoria)
            producto.save()

                # Redirige de vuelta al formulario de Stock con el producto seleccionado.
            return redirect('stock_create_from_producto', producto_id=producto.pk)
    else:
        form = ProductoForm(initial={'categoria_existente': categoria})

    return render(request, 'stock/producto_nuevo.html', {'form': form})


def producto_create_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)  # No guardamos el producto todavía
            categoria_nueva = form.cleaned_data.get('categoria_nueva')  # Obtenemos la nueva categoría ingresada
            if categoria_nueva:
                # Si se ingresó una nueva categoría, la creamos y la asignamos al producto
                nueva_categoria = Categoria.objects.create(nombre=categoria_nueva)
                producto.categoria.add(nueva_categoria)
            producto.save()  # Ahora guardamos el producto

            # Redirige de vuelta al formulario de Stock con el producto seleccionado.
            return redirect('stock_create_from_producto', producto_id=producto.pk)
    else:
        form = ProductoForm()

    return render(request, 'stock/producto_nuevo.html', {'form': form})

def proveedor_create_view(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save()
            # Redirige de vuelta al formulario de Stock con el proveedor seleccionado.
            return redirect('stock_create_from_proveedor', proveedor_id=proveedor.pk)
    else:
        form = ProveedorForm()

    return render(request, 'stock/proveedor_nuevo.html', {'form': form})

def categoria_create_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            # Redirige de vuelta al formulario de Producto con la categoria seleccionada.
            return redirect('producto_create_from_categoria', categoria_id=categoria.pk)
    else:
        form = CategoriaForm()

    return render(request, 'stock/categoria_nueva.html', {'form': form})


# Ejemplo de vista Django para procesar códigos de barras y QR
"""import cv2
import numpy as np
from pyzbar.pyzbar import decode

def scan_codes(request):
    if request.method == 'POST':
        image = request.FILES['image'].read()
        decoded_objects = decode(cv2.imdecode(np.fromstring(image, np.uint8), cv2.IMREAD_GRAYSCALE))
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            if obj.type == 'QRCODE':
                # Acción para códigos QR
                pass
            elif obj.type == 'CODE128':
                # Acción para códigos de barras
                pass
    return render(request, 'scan_codes.html')"""
