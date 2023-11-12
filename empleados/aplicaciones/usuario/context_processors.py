from aplicaciones.pedido.models import Pedido
from aplicaciones.categoria.models import Categoria
from notifications.models import Notification

def carrito_info(request):
    carrito_info = {'cantidad_del_carrito': 0}
    if request.user.is_authenticated:
        usuario = request.user
        pedido, created = Pedido.objects.get_or_create(usuario=usuario)
    # Aquí, obtén la información del carrito y devuelve un diccionario con los datos relevantes.
        if pedido:
            carrito_info = {
            'cantidad_del_carrito': pedido.get_cart_items,
        # Otras datos del carrito
    }
    return {'carrito_info': carrito_info}


def categorias_context(request):
    categorias = Categoria.objects.all()
    return {
        'categorias': categorias,
    }

def notificaciones_lista_context(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    else:
        notifications = [] 
    return {'notifications': notifications}
