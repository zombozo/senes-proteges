from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(transaccion)
admin.site.register(pago)
admin.site.register(servicioExterno)
admin.site.register(cobro)
admin.site.register(donacion)
admin.site.register(donante)