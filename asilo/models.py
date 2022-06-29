
import uuid
from django.db import models


# Create your models here.


class expediente(models.Model):
    id_expediente = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    id_datosPersonales = models.ForeignKey("usuarios.datosPersonales", unique=True, related_name="expediente_datosPersonales", on_delete=models.CASCADE)
    codigo_expediente = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id_datosPersonales.primer_nombre}"
        

class contacto(models.Model):
    id_contacto = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    id_expediente = models.ForeignKey("asilo.expediente", verbose_name=("expediente"), on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    numero_telefono = models.CharField(max_length=8)
    correo_electronico = models.EmailField(max_length=254, blank=True, null=True)
    parentesco = models.CharField(max_length=50, null=False, blank=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.parentesco

class cuenta(models.Model):
    id_cuenta = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    id_expediente = models.ForeignKey("asilo.expediente", verbose_name=("Expediente"), on_delete=models.CASCADE)
    deuda = models.BooleanField(default=0 )
    creado_en = models.DateTimeField(auto_now=True)

class transaccion(models.Model):
    id_transaccion = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    id_cuenta = models.ForeignKey("asilo.cuenta", verbose_name=("cuenta"), on_delete=models.CASCADE)
    id_factura = models.ForeignKey("fundacion.factura", related_name="transaccion_factura", verbose_name=("Seleccione la factura:"), on_delete=models.CASCADE)
    monto = models.FloatField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)




