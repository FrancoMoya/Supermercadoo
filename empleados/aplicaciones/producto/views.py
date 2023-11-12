from django.shortcuts import render
from .models import Producto
from aplicaciones.pedido.models import Pedido
from aplicaciones.carrito.models import *

def productos (request):
    
    productos = Producto.objects.all()
    return render(request, 'producto/productos.html', {
        'productos': productos,
    })
    
def productosItems (request):
    if request.user.is_authenticated:
        usuario = request.user
        pedido, created = Pedido.objects.get_or_create(usuario=usuario)
        cartItems = pedido.get_cart_items
    else:
        items = []
        pedido = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = pedido['get_cart_items']
    return render(request, 'usuario/base.html', {
        'cartItems': cartItems,
    })