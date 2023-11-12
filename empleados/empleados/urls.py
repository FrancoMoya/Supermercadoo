"""
URL configuration for empleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from aplicaciones.usuario.views import home, registro, cerrar_sesion, iniciar_sesion
from aplicaciones.carrito.views import updateItem, carrito, pago, verificar_cupon
from aplicaciones.producto.views import productos, productosItems
from aplicaciones.categoria.views import categorias
from aplicaciones.descuentos.views import *
from aplicaciones.stock import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('', home, name = 'home'),
    path('registro/', registro, name = 'registro'),
    path('productos/', productos, name = 'productos'),
    path('productosItems/', productosItems, name = 'productosItems'),
    path('logout/', cerrar_sesion, name = 'logout'),
    path('login/', iniciar_sesion, name = 'login'),
    path('update_item/', updateItem, name = 'updateItem'),
    path('carrito/', carrito, name = 'carrito'),
    path('pago/', pago, name = 'pago'),
    path('categorias/<str:nombre_categoria>/', categorias, name = 'categorias'),
    path('notificaciones/', notificaciones_lista, name='notificaciones_lista'),
    path('notificaciones/<int:notificacion_id>/', notificacion_detalle, name='notificacion_detalle'),
    path('crear_cupon/', crear_cupon, name='crear_cupon'),
    path('verificar_cupon/', verificar_cupon, name='verificar_cupon'),
    path('stock/create/', views.StockCreateView.as_view(), name='stock_create'),
    path('stock/create/producto/<int:producto_id>/', views.stock_create_from_producto, name='stock_create_from_producto'),
    path('stock/create/proveedor/<int:proveedor_id>/', views.stock_create_from_proveedor, name='stock_create_from_proveedor'),
    path('producto/create/', views.producto_create_view, name='producto_create'),
    path('producto/create/from_categoria/<int:categoria_id>/', views.producto_create_from_categoria, name='producto_create_from_categoria'),
    path('proveedor/create/', views.proveedor_create_view, name='proveedor_create'),
    path('categoria/create/', views.categoria_create_view, name='categoria_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
