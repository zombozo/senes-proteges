from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(datosPersonales)
admin.site.register(usuario)
admin.site.register(empleado)
admin.site.register(empleadoEspecialidad)