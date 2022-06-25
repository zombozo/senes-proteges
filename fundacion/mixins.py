from fundacion.models import consultaMedica, factura, facturaDetalleEspecialidad, facturaDetalleFarmacia, ficha, tratamiento


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
        
    
    
    