from django.db.models import signals
from django.dispatch import receiver
from aplicaciones.descuentos.models import Cupon
from aplicaciones.descuentos.views import *

@receiver(signals.post_save, sender=Cupon)
def cupon_creado(sender, instance, created, **kwargs):
    if created:
        notificar_a_todos_los_usuarios_sobre_cupon(instance)
