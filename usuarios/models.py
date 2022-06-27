from datetime import datetime
import logging
from random import choices
from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class datosPersonales(models.Model):
    id_datosPersonales = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=20, blank=True, null=True)
    primer_apellido = models.CharField(max_length=20, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    dni = models.CharField(max_length=13, blank=False, null=False, unique=True)
    creado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.primer_nombre} {self.primer_apellido}"


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
    usuario = models.ForeignKey("usuarios.usuario", unique=True, related_name="usuario_empleado", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.id_empleado_especialidad.nombre} {self.id_datos_personales.primer_nombre} {self.id_datos_personales.primer_apellido}"



class empleadoEspecialidad(models.Model):
    id_empleado_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    actividades = models.TextField(("Actividades de la especialialidad"))

    def __str__(self) -> str:
        return f"{self.id_empleado_especialidad} {self.nombre}"


class UserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_staff, is_superuser, is_admin, **extra_fields
        ):
        if not email:
            raise ValueError("No se agrego correo electronico")
        now = timezone.now()
        email = self.normalize_email(email)
        print(f"{now} {email} {password} {is_staff} {is_superuser} {is_admin}")
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            is_admin=is_admin,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        
    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email, password, False, False, False, **extra_fields
        )
        
    def create_superuser(self, email, password, **extra_fields):
        
        user = self._create_user(
            email, password, True, True, True, **extra_fields
        )
        user.save(using=self._db)
        return user
        
    def create_admin(self, email, password, **extra_fields):
        user = self._create_user(
            email, password, False, True, True, **extra_fields
        )
        user.save(using=self._db)
        return user

class usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField( max_length=254, unique=True)
    username = models.CharField(
        max_length=254, null=True, blank=True, unique=True
    )
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = UserManager()
    REQUIRED_FIELDS = ["username"]
    

    def __str__(self):
        return self.email