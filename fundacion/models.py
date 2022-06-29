
from django.db import models

from asilo.models import expediente, transaccion

# Create your models here.

class factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("ficha"), related_name="factura_ficha", on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.nit} {self.fecha}"
        
    def get_facturas_por_cliente(_expediente):
        pass
    
    def pendiente_de_pagar(self):
        transacciones = transaccion.objects.filter(id_factura=self.id_factura)

class facturaDetalleEspecialidad(models.Model):
    id_facturaDetalle = models.AutoField(primary_key=True)
    id_factura = models.ForeignKey("fundacion.factura", related_name=("factura_detalle"), on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey("fundacion.especialidad", verbose_name=("especialidad"), on_delete=models.CASCADE)
    costo = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.id_especialidad.especialidad} Q.{self.costo}"

class facturaDetalleFarmacia(models.Model):
    id_facturaDetalleFarmacia = models.AutoField(primary_key=True)
    id_factura = models.ForeignKey("fundacion.factura", related_name=("farmacia_detalle"), on_delete=models.CASCADE)
    id_medicamento = models.ForeignKey("fundacion.medicamento", verbose_name=("medicamento"), on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()

estados = [
        (1,"Pendiente"),
        (2,"Entregado"),
        (3,"Sin existencia"),
        (4,"No se presento ")
        ]

class tratamiento(models.Model):
        id_tratamiento = models.AutoField(primary_key=True)
        id_ficha = models.ForeignKey("fundacion.ficha", related_name="tratamiento_ficha", on_delete=models.CASCADE)
        fecha = models.DateField(("Fecha de Inicio"), auto_now=True)
        medicamento =models.ForeignKey("fundacion.medicamento", verbose_name=("Seleccionar el medicamento"), on_delete=models.CASCADE)
        cantidad = models.IntegerField(null=True, blank=True)
        id_enfermedad = models.ForeignKey("fundacion.enfermedad", blank=True, null=True, verbose_name=("Seleccione la enfermedad"), on_delete=models.CASCADE)
        descripcion = models.TextField(null=False, blank=False)
        estado = models.IntegerField(choices=estados, default=1)

class enfermedad(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class medicamento(models.Model):
        id_medicamento = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50, null=False, blank=False)
        dosis = models.CharField(max_length=50, null=False, blank=False)
        administracion = models.ForeignKey("fundacion.viaAdministracion", verbose_name=("Via de administracion"), on_delete=models.CASCADE)
        precio = models.FloatField()
        
        def __str__(self):
            return f"{self.nombre} {self.dosis} {self.administracion}"

class viaAdministracion(models.Model):
    id_viaAdministracion = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50, blank=False, null=False)

class horarioAtencion(models.Model):
    id_horarioAtencion = models.AutoField(primary_key=True)
    id_especialidad = models.ForeignKey("fundacion.especialidad", verbose_name=("Especialidad: "), on_delete=models.CASCADE)
    id_rango = models.ForeignKey("fundacion.rangoHorario",verbose_name=("Dias de atencion: "), on_delete=models.CASCADE)
    hora_apertura = models.TimeField(("horario_apertura"), null=True, blank=True)
    hora_cierre = models.TimeField()

class rangoHorario(models.Model):
    id_rangoHorario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre = models.CharField(("nombre"), max_length=50)
    
    def __str__(self):
        return self.nombre

class especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    id_area = models.ForeignKey("fundacion.area", null=True, blank=True, verbose_name=("Area: "), related_name="especialidad_area", on_delete=models.CASCADE)
    costo = models.FloatField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.especialidad}"

class laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("Ficha"), related_name="laboratorio_ficha", on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey("fundacion.especialidad", verbose_name=("Especialidad: "), on_delete=models.CASCADE)
    fecha_hora = models.DateField(("Fecha y hora"), auto_now=True)
    resultado = models.CharField(max_length=50, null=True, blank=True)
    descripcion_muestra = models.CharField(("Describa la muestra"), max_length=50)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.resultado

class solicitudLaboratorio(models.Model):
        id_solicitudLaboratorio = models.AutoField(primary_key=True)
        id_empleado = models.ForeignKey("usuarios.empleado", null=True, verbose_name=("Medico solicitante"), on_delete=models.CASCADE)
        id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("ficha"),on_delete=models.CASCADE)
        id_especialidad = models.ForeignKey('fundacion.especialidad', related_name='especialidad_Sollaboratorio', verbose_name="Especialidad: ", on_delete=models.CASCADE)
        descripcion = models.TextField(null=True, blank=True)
        fecha_hora = models.DateField(("fecha y hora"), auto_now=True)
        creado_en= models.DateTimeField(auto_now=True)
        aceptado = models.BooleanField(default=False)

class ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    id_expediente = models.ForeignKey('asilo.expediente', related_name='ficha_expediente', on_delete=models.CASCADE)
    fecha = models.DateField( auto_now=True)
    id_solicitudCita = models.ForeignKey('fundacion.solicitudCita', related_name='ficha_solicitud', on_delete=models.CASCADE)

    def get_ficha(form=None, _solicitudCitaDetalle=None):
        _ficha = ficha()
        if _solicitudCitaDetalle != None:
            try:
                _ficha = ficha.objects.get(id_solicitudCita=_solicitudCitaDetalle.id_solicitudCita.id_solicitudCita)
            except solicitudCitaDetalle.DoesNotExist:
                _ficha = None
            except ficha.DoesNotExist:
                _ficha.id_solicitudCita = _solicitudCitaDetalle.id_solicitudCita
                _ficha.id_expediente = _solicitudCitaDetalle.id_solicitudCita.id_expediente
                _ficha.save()
        elif form != None:
            try:
                _ficha = ficha.objects.get(id_expediente=form.instance.id_solicitudCitaDetalle.id_solicitudCita.id_expediente.id_expediente)
            except Exception as e:
                _expediente = expediente.objects.get(id_expediente=form.instance.id_solicitudCitaDetalle.id_solicitudCita.id_expediente.id_expediente)
                _ficha.id_solicitudCita=form.instance.id_solicitudCitaDetalle.id_solicitudCita
                _ficha.id_expediente =_expediente
                _ficha.save()
        return _ficha

    def get_factura(self):
        return factura.objects.filter(id_ficha=self.id_ficha)

    def get_facturas_pendientes(self):
        facturas = factura.objects.filter(id_ficha=self.id_ficha)
        return [factura for factura in facturas if factura.pendiente_de_pagar()]

class solicitudCita(models.Model):
    id_solicitudCita = models.AutoField(primary_key=True)
    id_expediente = models.ForeignKey('asilo.expediente', related_name='expediente_solicitudCita', on_delete=models.CASCADE)
    id_enfermero = models.ForeignKey("usuarios.empleado", verbose_name="Asignar Enfermero: ", on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripcion de la consulta General: ")
    creado_en = models.DateTimeField(auto_now=True)
    solicitud_finalizada = models.BooleanField(default=False)
    aceptada = models.BooleanField(default=False)

class solicitudCitaDetalle(models.Model):
    solicitudCitaDetalle = models.AutoField(primary_key=True)
    id_solicitudCita = models.ForeignKey("fundacion.solicitudCita", verbose_name=("solicitud"), related_name="detalle_cita", on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey("fundacion.especialidad", verbose_name="Especialidad: ", on_delete=models.CASCADE)
    descripcion = models.TextField(("Descripcion de la solicitud"))
    fecha_hora = models.DateTimeField(("horario de la cita"), null=True, blank=True)
    aceptado = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.fecha_hora != None:
            self.aceptado=True
        super(solicitudCitaDetalle, self).save(*args, **kwargs) 

class consultaMedica(models.Model):
    id_consultaMedica = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey("fundacion.ficha", verbose_name=("ficha"), related_name="consulta_ficha", on_delete=models.CASCADE)
    id_solicitudCitaDetalle = models.ForeignKey("fundacion.solicitudCitaDetalle", verbose_name=("consulta_solicitudDetalle"), related_name='consulta_SolicitudDetalle', on_delete=models.CASCADE)
    diagnostico = models.TextField()
    creado_en = models.DateTimeField(auto_now=True)
    
    
    