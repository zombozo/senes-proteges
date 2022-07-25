import json
from django.conf import settings
from asilo.models import contacto
from contabilidad.models import cobro, donacion, pago
from fundacion.models import clienteEnfermedad
from reportes.controlErrores import get_loggerSenes
from reportes.correoElectronico import correo
from django.db.models import Count, Sum


class medicoMixin(object):
    def __init__(self) -> None:
        pass
    
    
    def enviar_correo(self, _solicitudCita):
        _correo = correo()
        try:
            _contacto = contacto.objects.filter(id_expediente=_solicitudCita.id_expediente.id_expediente)[0:1].get()
            contenido = {
                "solicitudes":_solicitudCita
            }
            _correo.set_contenidoCorreo(
                destinatario=settings.EMAIL_HOST_USER,
                subject="Consulta medica",
                contexto=contenido,
                to=[_contacto.correo_electronico]
            )
            _correo.enviar(contexto=contenido)
            print(f"correo electronico enviado por {settings.EMAIL_HOST_USER} al correo {_contacto.correo_electronico}")
        except contacto.DoesNotExist as e:
            logger = get_loggerSenes()
            logger.info(e.__traceback__)
        pass
    
class asiloMixin(object):
    def __init__(self) -> None:
        pass
    
    
    def get_context_for_home(self):
        enfermedades = []
        flujo_de_caja = {}
        context = {}
        enfermedades = (clienteEnfermedad.objects.values('id_enfermedad__nombre').annotate(dcount=Count('id_enfermedad'))).order_by()
        print(enfermedades)
        pagos = pago.objects.values("id_transaccion__monto").aggregate(pagos=Sum('id_transaccion__monto'))
        cobros = cobro.objects.values('id_transaccion__monto').aggregate(cobros=Sum('id_transaccion__monto'))
        donaciones = donacion.objects.values('id_transaccion__monto').aggregate(donaciones=Sum('id_transaccion__monto'))
        flujo_de_caja.update(pagos)
        flujo_de_caja.update(cobros)
        flujo_de_caja.update(donaciones)
        print(flujo_de_caja)
        context['flujo_caja']=json.dumps(flujo_de_caja)
        context["enfermedades"]=json.dumps(list(enfermedades))
        return context