from cgitb import handler
import logging
from asilo.models import expediente
from fundacion.forms import consultaMedicaForm
from fundacion.models import consultaMedica, factura,solicitudLaboratorio, facturaDetalleEspecialidad, facturaDetalleFarmacia, ficha, solicitudCita, solicitudCitaDetalle, tratamiento
from reportes.controlErrores import get_loggerSenes




class medicoMixin(object):
    def get_context_data(self, **kwargs):
        context = super(medicoMixin, self).get_context_data(**kwargs)
        return context
        
    # def get_citas(self):
    #     resultados = 
    
    
class facturaMixin:
    def __init__(self) -> None:
        self.factura = None
        self.ficha = None
        
    
    def set_detalleFarmacia(self):
        tratamientos = tratamiento.objects.filter(id_ficha=self.ficha.id_ficha)
        for _tratamiento in tratamientos:
            detalle_farmacia = facturaDetalleFarmacia()
            detalle_farmacia.id_factura = self.factura.id_factura
            detalle_farmacia.id_medicamento = _tratamiento.id_medicamento
            detalle_farmacia.cantidad = _tratamiento.cantidad
            detalle_farmacia.precio_unitario = _tratamiento.medicamento.precio
            detalle_farmacia.save()
        
    def set_detalleEspecialidades(self):
        consultas = consultaMedica.objects.filter(id_ficha=self.ficha.id_ficha)
        for consulta in consultas:
            detalle = facturaDetalleEspecialidad()
            detalle.id_especialidad=consulta.id_solicitudCitaDetalle.id_especialidad
            detalle.costo = consulta.id_solicitudCitaDetalle.id_especialidad.costo
            detalle.id_factura = self.factura
            detalle.save()
        
    def crear_detalle(self, id_factura, _ficha):
        try:
            self.factura = factura.objects.get(id_factura=id_factura)
            self.ficha = ficha.objects.get(id_ficha=_ficha)
            print(f"---> {self.ficha}")
            self.set_detalleFarmacia()
            self.set_detalleEspecialidades()
        except print(0):
            pass
        
    
class recepcionMixin(object):
        def get_contexto(self):
            contexto = {}
            print(self.request.GET)
            if self.request.GET.get("pagina"):
                if self.request.GET.get("pagina") == "clientes":
                    contexto['pagina']="clientes"
                    contexto["clientes"]= expediente.objects.all()
            else:
                contexto['pagina']="clientes"
                contexto["clientes"]= expediente.objects.all()
            return contexto
            

class consultaMedicaMixin(object):

    def get_contexto(self):
        id_expediente = self.kwargs["id_expediente"]
        id_detalle = self.request.GET.get("detalle")
        _solicitud = solicitudCitaDetalle.objects.get(solicitudCitaDetalle=id_detalle)
        data ={'id_solicitudCitaDetalle':_solicitud}
        form  = consultaMedicaForm(initial=data)
        
        context= {
            "solicitud_detalle":_solicitud,
            "form":form,
            "expediente": expediente.objects.get(id_expediente=id_expediente)
        }
        try:
            _ficha = ficha.objects.get(id_solicitudCita=_solicitud.id_solicitudCita.id_solicitudCita)
            tratamientos = tratamiento.objects.filter(id_ficha=_ficha.id_ficha)
            context["tratamientos"] = tratamientos
            context["solicitud"] = solicitudCita.objects.get(id_solicitudCita=_solicitud.id_solicitudCita.id_solicitudCita)
            context["solicitudLaboratorio"] = solicitudLaboratorio.objects.filter(id_solicitudCita=_solicitud.id_solicitudCita.id_solicitudCita)
            print(f"contexto {context}")
        except Exception as e:
            logerSenes = get_loggerSenes()
            logerSenes.debug(e)
        
        return context
        