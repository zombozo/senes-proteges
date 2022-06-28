

from django.conf import settings
from asilo.models import contacto
from reportes.correoElectronico import correo


class medicoMixin(object):
    def __init__(self) -> None:
        pass
    
    
    def enviar_correo(self, _solicitudCita):
        _correo = correo()
        contacto = contacto.objects.get(id_expediente=_solicitudCita.id_expediente.id_expediente)
        contenido = {
            "solicitudes":_solicitudCita
        }
        _correo.set_contenidoCorreo(
            destinatario=settings.EMAIL_HOST_USER,
            subject="Consulta medica",
            contexto=contenido,
            to=[contacto.correo_electronico]
        )
        _correo.enviar(contexto=contenido)
        pass