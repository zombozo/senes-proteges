from django.conf import settings
from asilo.models import contacto
from reportes.controlErrores import get_loggerSenes
from reportes.correoElectronico import correo


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
        except contacto.DoesNotExist as e:
            logger = get_loggerSenes()
            logger.info(e.__traceback__)
        pass