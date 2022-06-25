from random import choices
from django.db import models

# Create your models here.
class datosPersonales(models.Model):
    id_datosPersonales = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=20, blank=True, null=True)
    primer_apellido = models.CharField(max_length=20, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    dni = models.BigIntegerField(blank=False, null=False)
    creado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.primer_nombre


    def get_nombreCompleto(self):
        return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"

empresas = (
    ("1","fundacion"),
    ("2","asilo")
)
class empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_datos_personales = models.ForeignKey("usuarios.datosPersonales", verbose_name=("Datos personales"), on_delete=models.CASCADE)
    id_empleado_especialidad = models.ForeignKey("usuarios.empleadoEspecialidad", verbose_name=("Especialidad"), on_delete=models.CASCADE)
    empresa = models.CharField(max_length=80, choices=empresas)
    
    def __str__(self) -> str:
        return f"{self.id_empleado_especialidad.nombre} {self.id_datos_personales.primer_nombre} {self.id_datos_personales.primer_apellido}"



class empleadoEspecialidad(models.Model):
    id_empleado_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    actividades = models.TextField(("Actividades de la especialialidad"))

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=12)
    contrasena = models.CharField(max_length=50)
    datos_personales = models.ForeignKey("usuarios.datosPersonales", on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, null=False, blank=False)
    permisos = models.TextField()
    

    def __str__(self):
        return self.usuario
