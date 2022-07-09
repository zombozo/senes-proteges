from django.db import models
from fundacion.models import factura

# Create your models here.
class transaccion(models.Model):
    id_transaccion = models.BigAutoField(primary_key=True)
    monto = models.FloatField()
    fecha = models.DateTimeField(auto_now=True)

class pago(models.Model):
    id_pago = models.BigAutoField(primary_key=True)
    id_servicio = models.ForeignKey('contabilidad.servicioExterno', related_name='servicio_pago', on_delete=models.CASCADE)
    id_transaccion = models.ForeignKey('contabilidad.transaccion', related_name='transaccion_pago', on_delete=models.CASCADE)

class servicioExterno(models.Model):
    id_servicioExterno = models.BigAutoField(primary_key=True)
    nombre  = models.CharField(max_length=150)
    empresa = models.name = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"

class cobro(models.Model):
    id_factura= models.ForeignKey('fundacion.factura', related_name='cobro_factura', on_delete=models.CASCADE)
    id_transaccion = models.ForeignKey('contabilidad.transaccion', related_name='cobro_transaccion', on_delete=models.CASCADE)

    def set_cobro(transaccion, id_factura):
        _cobro = cobro()
        _cobro.id_factura = factura.objects.get(id_factura=id_factura)
        _cobro.id_transaccion = transaccion
        _cobro.save()

    def __str__(self):
        return f"{self.id_transaccion.monto} "

class donacion(models.Model):
    id_donacion = models.BigAutoField(primary_key=True)
    nombre  = models.CharField(max_length=100)
    id_donante = models.ForeignKey('contabilidad.donante', related_name='donante_donacion', on_delete=models.CASCADE)
    id_transaccion = models.ForeignKey('contabilidad.transaccion', related_name='transaccion_donacion', on_delete=models.CASCADE)
    
class donante(models.Model):
    id_donante = models.BigAutoField(primary_key=True)
    tipo  = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo