
import uuid
from django.db import models
from django.template.defaultfilters import slugify




# Create your models here.


class expediente(models.Model):
    id_expediente = models.BigAutoField(primary_key=True)
    id_datosPersonales = models.ForeignKey("usuarios.datosPersonales", unique=True, related_name="expediente_datosPersonales", on_delete=models.CASCADE)
    codigo_expediente = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id_datosPersonales.primer_nombre}"

    def save(self, *args, **kwargs):
        super(expediente, self).save(*args, **kwargs)
        if self.codigo_expediente is None:
            self.codigo_expediente = slugify(f"SP-{self.id_expediente}")
            self.save()

    def get_expediente(datosPersonales):
        exp = expediente()
        exp.id_datosPersonales = datosPersonales
        exp.save()
        return exp

class contacto(models.Model):
    id_contacto = models.BigAutoField(primary_key=True)
    id_expediente = models.ForeignKey("asilo.expediente", related_name="contacto_expediente", verbose_name=("expediente"), on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    numero_telefono = models.CharField(max_length=8)
    correo_electronico = models.EmailField(max_length=254, blank=True, null=True)
    parentesco = models.CharField(max_length=50, null=False, blank=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.parentesco} {self.id_expediente.id_datosPersonales.primer_nombre} {self.correo_electronico}"

class cuenta(models.Model):
    id_cuenta = models.BigAutoField(primary_key=True)
    id_expediente = models.ForeignKey("asilo.expediente", verbose_name=("Expediente"), on_delete=models.CASCADE)
    deuda = models.BooleanField(default=0 )
    creado_en = models.DateTimeField(auto_now=True)





