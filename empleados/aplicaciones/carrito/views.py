from django.shortcuts import render
from django.http import JsonResponse
import json
from aplicaciones.pedido.models import Pedido
from aplicaciones.descuentos.models import Cupon
from aplicaciones.producto.models import Producto
from .models import Carrito

def carrito(request):
    if request.user.is_authenticated:
        usuario = request.user
        pedido, created = Pedido.objects.get_or_create(usuario=usuario)
        items = pedido.carrito_set.all()
        # pedido es la foreign key de carrito
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'carrito/carrito.html', context)

def pago(request):
    if request.user.is_authenticated:
        usuario = request.user
        pedido, created = Pedido.objects.get_or_create(usuario=usuario)
        items = pedido.carrito_set.all()
        # pedido es la foreign key de carritoproducto
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'carrito/pago.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('Producto ID:', productId)
    
    usuario = request.user
    print(usuario)
    producto = Producto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create(usuario=usuario)
    carrito, created = Carrito.objects.get_or_create(pedido=pedido, producto=producto)
    
    if action == 'add':
        carrito.cantidad = (carrito.cantidad + 1)
    elif action == 'remove':
        carrito.cantidad = (carrito.cantidad - 1)
    carrito.save()
    
    if carrito.cantidad <= 0:
        carrito.delete()
    
    return JsonResponse('Item was added', safe=False)

def verificar_cupon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cupon_codigo = data.get('cupon_codigo')  # Obtiene el código de cupón del cuerpo de la solicitud
        usuario = request.user
        pedido, created = Pedido.objects.get_or_create(usuario=usuario)
        
        print('Cupón recibido:', cupon_codigo)  # Registra el código de cupón recibido
        
        try:
            cupon = Cupon.objects.get(codigo=cupon_codigo)  # Verifica si el cupón existe
            # Agrega un print para verificar el código del cupón ingresado
            print('Código del cupón:', cupon_codigo)
            # Agrega un print para verificar si el usuario está autenticado
            print('Usuario autenticado:', request.user.is_authenticated)
            if cupon.compartido or usuario in cupon.usuarios_asociados.all():
                # El cupón es compartido o el usuario está en la lista de usuarios asociados
                # Aplicar el descuento aquí
                # Aplica el descuento al total del carrito
                total_carrito = pedido.get_cart_total
                if cupon.descuento_porcentaje is not None:
                    descuento = f"{((total_carrito * cupon.descuento_porcentaje) / 100)} ({cupon.descuento_porcentaje}%)"
                    nuevo_total = total_carrito - ((total_carrito * cupon.descuento_porcentaje) / 100)
                    total_anterior = total_carrito
                elif cupon.descuento_valor is not None:
                    # El cupón tiene un descuento en valor
                    descuento = cupon.descuento_valor
                    nuevo_total = total_carrito - cupon.descuento_valor
                    total_anterior = total_carrito
                else:
                    # El cupón no tiene un descuento válido
                    return total_carrito  # No se aplica ningún descuento
                # Guarda el descuento en el carrito o en el pedido si es necesario
                # pedido.descuento = descuento
                # pedido.save()
                return JsonResponse({'valid': True, 'descuento': descuento, 'nuevo_total': nuevo_total, 'total_anterior': total_anterior})
            else:
                # El cupón no es compartido y el usuario no está en la lista de usuarios asociados
                return JsonResponse({'valid': False, 'error': 'Cupón no válido'})
            
        except Cupon.DoesNotExist:
            print('Excepción: El cupón no existe')
            return JsonResponse({'valid': False, 'error': 'El cupón no existe'})

    return JsonResponse({'valid': False, 'error': 'Solicitud no válida'})

