
import uuid
from django.db import models

from asilo.models import expediente
from reportes.controlErrores import get_loggerSenes

# Create your models here.

class factura(models.Model):
    id_factura = models.BigAutoField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("ficha"), unique=True, related_name="factura_ficha", on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)

    def get_factura(id_ficha):
        return factura.objects.get_or_create(id_ficha=id_ficha)

    def __str__(self):
        return f"{self.id_factura} - cliente: {self.id_ficha.id_expediente.id_datosPersonales.get_nombreCompleto()} Nit:{self.nit} Fecha: {self.fecha}"
        
    def get_facturas_por_cliente(_expediente):
        pass
    
    def pendiente_de_pagar(self):
        transacciones = transaccion.objects.filter(id_factura=self.id_factura)

class facturaDetalleEspecialidad(models.Model):
    id_facturaDetalle = models.BigAutoField(primary_key=True)
    id_factura = models.ForeignKey("fundacion.factura", related_name=("factura_detalle"), on_delete=models.CASCADE)
    id_solicitudCitaDetalle = models.ForeignKey("fundacion.solicitudCitaDetalle", unique=True, verbose_name=("especialidad"), related_name="detalleSolicitud_factura", on_delete=models.CASCADE)
    costo = models.FloatField()
    descuento = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.id_solicitudCitaDetalle.id_especialidad.especialidad} Q.{self.costo}"

    def save_factura_detalle(consulta):
        _factura, status=factura.get_factura(consulta.id_ficha)
        factura_detalle = facturaDetalleEspecialidad()
        factura_detalle.id_factura = _factura
        factura_detalle.id_solicitudCitaDetalle = consulta.id_solicitudCitaDetalle
        factura_detalle.costo = consulta.id_solicitudCitaDetalle.id_especialidad.costo
        try:
            descuento = descuentoArea.objects.get(id_area__nombre="clinica")
            factura_detalle.descuento = descuento.porcentaje
        except Exception as e:
            logger = get_loggerSenes()
            logger.error("No se encontro un descuento valido para agregar")
        factura_detalle.save()

class facturaDetalleLaboratorio(models.Model):
    id_facturaDetalleLaboratorio = models.BigAutoField(primary_key=True)
    id_factura = models.ForeignKey("fundacion.factura", related_name=("factura_detalleLaboratorio"), on_delete=models.CASCADE)
    id_solicitudLaboratorio = models.ForeignKey("fundacion.solicitudLaboratorio", unique=True, verbose_name=("tipo de laboratorio"), related_name="detalleSolicitudLaboratorio_factura", on_delete=models.CASCADE)
    costo = models.FloatField()
    descuento = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.id_solicitudLaboratorio.id_tipoLaboratorio.nombre} Q.{self.costo}"

    def save_factura_detalleLaboratorio(consulta):
        _factura, status=factura.get_factura(consulta.id_ficha)
        factura_detalle = facturaDetalleLaboratorio()
        factura_detalle.id_factura = _factura
        factura_detalle.id_solicitudLaboratorio = consulta.id_solicitudLaboratorio
        factura_detalle.costo = consulta.id_solicitudLaboratorio.id_tipoLaboratorio.precio
        try:
            descuento = descuentoArea.objects.get(id_area__nombre="laboratorio")
            factura_detalle.descuento = descuento.porcentaje
        except Exception as e:
            logger = get_loggerSenes()
            logger.error("No se encontro un descuento valido para agregar")
        factura_detalle.save()

class facturaDetalleFarmacia(models.Model):
    id_facturaDetalleFarmacia = models.BigAutoField(primary_key=True)
    id_factura = models.ForeignKey("fundacion.factura", related_name=("farmacia_detalle"), on_delete=models.CASCADE)
    id_tratamiento = models.ForeignKey("fundacion.tratamiento", verbose_name=("tratamiento"), related_name="facturaDetalle_tratamiento", on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    descuento = models.IntegerField(blank=True, null=True)

    def set_detalleFactura(tratamiento):
        _factura, status= factura.get_factura(tratamiento.id_ficha)
        _ficha = ficha.get_factura(tratamiento.id_ficha)
        detalle = facturaDetalleFarmacia()
        detalle.id_factura = _factura
        detalle.id_tratamiento = tratamiento
        detalle.cantidad = tratamiento.cantidad
        detalle.precio_unitario = tratamiento.medicamento.precio
        try:
            descuento = descuentoArea.objects.get(id_area__nombre="laboratorio")
            detalle.descuento = descuento.porcentaje
        except Exception as e:
            logger = get_loggerSenes()
            logger.error("No se encontro un descuento valido para agregar")
        detalle.save()

estados = [
        (1,"Pendiente"),
        (2,"Entregado"),
        (3,"Sin existencia"),
        (4,"No se presento ")
        ]

class tratamiento(models.Model):
        id_tratamiento = models.BigAutoField(primary_key=True)
        id_ficha = models.ForeignKey("fundacion.ficha", related_name="tratamiento_ficha", on_delete=models.CASCADE)
        fecha = models.DateField(("Fecha de Inicio"), auto_now=True)
        medicamento =models.ForeignKey("fundacion.medicamento", verbose_name=("Seleccionar el medicamento"), on_delete=models.CASCADE)
        cantidad = models.IntegerField()
        descripcion = models.TextField(null=False, blank=False)
        estado = models.IntegerField(choices=estados, default=1)

        def __str__(self):
            return self.medicamento.nombre
        
        def get_nombreCliente(self):
            return expediente.objects.get(id_expediente=self.id_ficha.id_expediente)
        
class clienteEnfermedad(models.Model):
    id_clienteEnfermedad = models.BigAutoField(primary_key=True)
    id_expediente = models.ForeignKey("asilo.expediente", related_name=("expediente_enfermedad"), on_delete=models.CASCADE)
    id_enfermedad = models.ForeignKey("fundacion.enfermedad", related_name="enfermedad_expediente", verbose_name=("enfermedad:"), on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)
    
    
class clienteEnfermedad(models.Model):
    id_clienteEnfermedad = models.BigAutoField(primary_key=True)
    id_expediente = models.ForeignKey("asilo.expediente", related_name=("expediente_enfermedad"), on_delete=models.CASCADE)
    id_enfermedad = models.ForeignKey("fundacion.enfermedad", related_name=("enfermedad_cliente"), on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

class enfermedad(models.Model):
    id_enfermedad = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
class medicamento(models.Model):
        id_medicamento = models.BigAutoField(primary_key=True)
        nombre = models.CharField(max_length=50, null=False, blank=False)
        dosis = models.CharField(max_length=50, null=False, blank=False)
        administracion = models.ForeignKey("fundacion.viaAdministracion", verbose_name=("Via de administracion"), on_delete=models.CASCADE)
        precio = models.FloatField()
        
        def __str__(self):
            return f"{self.nombre} {self.dosis} {self.administracion}"

class viaAdministracion(models.Model):
    id_viaAdministracion = models.BigAutoField(primary_key=True)
    nombre  = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.nombre
    
class horarioAtencion(models.Model):
    id_horarioAtencion = models.BigAutoField(primary_key=True)
    id_especialidad = models.ForeignKey("fundacion.especialidad", verbose_name=("Especialidad: "), on_delete=models.CASCADE)
    id_rango = models.ForeignKey("fundacion.rangoHorario",verbose_name=("Dias de atencion: "), on_delete=models.CASCADE)
    hora_apertura = models.TimeField(("horario_apertura"), null=True, blank=True)
    hora_cierre = models.TimeField()

class rangoHorario(models.Model):
    id_rangoHorario = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class area(models.Model):
    id_area = models.BigAutoField(primary_key=True)
    nombre = models.CharField(("nombre"), max_length=50)
    
    def __str__(self):
        return self.nombre

class especialidad(models.Model):
    id_especialidad = models.BigAutoField(primary_key=True)
    especialidad = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    id_area = models.ForeignKey("fundacion.area", null=True, blank=True, verbose_name=("Area: "), related_name="especialidad_area", on_delete=models.CASCADE)
    costo = models.FloatField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.id_area.nombre} - {self.especialidad}"

class laboratorio(models.Model):
    id_laboratorio = models.BigAutoField(primary_key=True)
    id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("Ficha"), related_name="laboratorio_ficha", on_delete=models.CASCADE)
    id_solicitudLaboratorio = models.ForeignKey("fundacion.solicitudLaboratorio", unique=True, verbose_name=("solicitud: "), related_name="laboratorio_solicitudDetalle", on_delete=models.CASCADE)
    fecha_hora = models.DateField(("Fecha y hora"), auto_now=True)
    tipo_muestra = models.ForeignKey('fundacion.tipoMuestra', verbose_name='tipo de muestra', related_name='tipo_muestra_laboratorio',null=True, blank=True, on_delete=models.CASCADE, )
    resultado = models.CharField(max_length=50, null=True, blank=True)
    descripcion_resultado = models.CharField(("Describa el resultado:"), null=True, blank=True, max_length=50)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.resultado}"

class tipoMuestra(models.Model):
    id_tipoMuestra = models.BigAutoField(primary_key=True)
    muestra = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.muestra
    
class tipoLaboratorio(models.Model):
    id_tipoLaboratorio = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    
class solicitudLaboratorio(models.Model):
    id_solicitudLaboratorio = models.BigAutoField(primary_key=True)
    id_solicitudCita = models.ForeignKey("fundacion.solicitudCita", verbose_name=("Asociada a la solicitud:"), on_delete=models.CASCADE)
    id_empleado = models.ForeignKey("usuarios.empleado", null=True, verbose_name=("Medico solicitante"), on_delete=models.CASCADE)
    id_tipoLaboratorio = models.ForeignKey('fundacion.tipoLaboratorio', related_name='solicitud_tipoLaboratorio', verbose_name="Tipo de laboratorio: ", on_delete=models.CASCADE)
    descripcion = models.TextField(null=True,verbose_name="Describa la solicitud:" ,blank=True)
    creado_en= models.DateTimeField(auto_now=True)
    aceptado = models.BooleanField(blank=True, null=True)

class ficha(models.Model):
    id_ficha = models.BigAutoField(primary_key=True)
    id_expediente = models.ForeignKey('asilo.expediente', related_name='ficha_expediente', on_delete=models.CASCADE)
    fecha = models.DateField( auto_now=True)
    id_solicitudCita = models.ForeignKey('fundacion.solicitudCita', related_name='ficha_solicitud', unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_expediente.id_datosPersonales.get_nombreCompleto()} el {self.fecha}"
    
    
    def get_ficha(_solicitudCitaDetalle=None):
        _ficha = ficha()
        if _solicitudCitaDetalle != None:
            try:
                _ficha = ficha.objects.get(id_solicitudCita=_solicitudCitaDetalle.id_solicitudCita)
            except solicitudCitaDetalle.DoesNotExist as e:
                print("**  -- solicitudCitaDetalle.DoesNotExist -- **")
                logger = get_loggerSenes()
                logger.info(e.with_traceback)
                _ficha = None
            except ficha.DoesNotExist as e:
                print("**  -- ficha.DoesNotExist -- **")
                logger = get_loggerSenes()
                logger.info(e.with_traceback)
                _ficha.id_solicitudCita = _solicitudCitaDetalle.id_solicitudCita
                _ficha.id_expediente = _solicitudCitaDetalle.id_solicitudCita.id_expediente
                _ficha.save()
        return _ficha

    def get_factura(self):
        return factura.objects.filter(id_ficha=self.id_ficha)

    def get_facturas_pendientes(self):
        facturas = factura.objects.filter(id_ficha=self.id_ficha)
        return [factura for factura in facturas if factura.pendiente_de_pagar()]

class solicitudCita(models.Model):
    id_solicitudCita = models.BigAutoField(primary_key=True)
    id_expediente = models.ForeignKey('asilo.expediente', related_name='expediente_solicitudCita', on_delete=models.CASCADE)
    id_enfermero = models.ForeignKey("usuarios.empleado", verbose_name="Asignar Enfermero: ", on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripcion de la consulta General: ")
    creado_en = models.DateTimeField(auto_now=True)
    solicitud_finalizada = models.BooleanField(default=False)

    def get_solicitud(id_expediente):
        try:
            solicitud = solicitudCita.objects.get(id_expediente=id_expediente, solicitud_finalizada=False)
            return True, solicitud.id_solicitudCita
        except solicitudCita.DoesNotExist as e:
            return False, 0
    
    def get_solicitudes_de_laboratorio(self):
        solicitudes = solicitudCitaDetalle.objects.filter(id_solicitudCita=self.id_solicitudCita, id_especialidad__id_area__nombre="Laboratorio")
        return solicitudes
    
    def get_solicitudes_consulta_medica(self):
        return solicitudCitaDetalle.objects.filter(id_solicitudCita=self.id_solicitudCita, id_especialidad__id_area__nombre="clinica")
    
    def get_solicitudesDetalle(self):
        _detalles = solicitudCitaDetalle.objects.filter(id_solicitudCita=self.id_solicitudCita, aceptada=None)
        return _detalles

class solicitudCitaDetalle(models.Model):
    solicitudCitaDetalle = models.BigAutoField(primary_key=True)
    id_solicitudCita = models.ForeignKey("fundacion.solicitudCita", verbose_name=("solicitud"), related_name="detalle_cita", on_delete=models.CASCADE)
    id_empleado = models.ForeignKey("usuarios.empleado", null=True, blank=True, verbose_name=("Empleado"),related_name="empleado_solicitud", on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey("fundacion.especialidad", verbose_name="Especialidad: ",related_name='especialidad_detalle',  on_delete=models.CASCADE)
    descripcion = models.TextField(("Descripcion de la solicitud"))
    fecha_hora = models.DateTimeField(("horario de la cita"), null=True, blank=True)
    aceptada = models.BooleanField(null=True, blank=True)
    
    def get_pendientes(self):
        solicitudes = solicitudCitaDetalle.objects.filter(aceptada=False)
        print(solicitudes)
        print("pase por solicitudes")
        return solicitudes
    
class motivoRechazo(models.Model):
    id_motivoRechazo = models.BigAutoField(primary_key=True)
    id_solicitudCitaDetalle = models.ForeignKey('fundacion.solicitudCitaDetalle', related_name='motivo_rechazo_detalleSolicitud', on_delete=models.CASCADE)
    motivo = models.TextField(default="")
    
class consultaMedica(models.Model):
    id_consultaMedica = models.BigAutoField(primary_key=True)
    id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("ficha"), related_name="consulta_ficha", on_delete=models.CASCADE)
    id_solicitudCitaDetalle = models.ForeignKey("fundacion.solicitudCitaDetalle", verbose_name=("consulta_solicitudDetalle"), related_name='consulta_SolicitudDetalle', on_delete=models.CASCADE)
    diagnostico = models.TextField()
    creado_en = models.DateTimeField(auto_now=True)

class descuentoArea(models.Model):
    id_descuento = models.BigAutoField(primary_key=True)
    id_area = models.OneToOneField("fundacion.area", verbose_name=("area"), unique=True, on_delete=models.CASCADE)
    porcentaje =models.IntegerField(verbose_name="Porcentaje de descuento para esta area")
    
    def __str__(self) -> str:
        return f"{self.id_area.nombre} - {self.porcentaje}%"