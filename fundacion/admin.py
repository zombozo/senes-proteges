from django.contrib import admin

from fundacion.models import *

# Register your models here.
admin.site.register(factura)
admin.site.register(facturaDetalleEspecialidad)
admin.site.register(facturaDetalleFarmacia)
admin.site.register(tratamiento)
admin.site.register(enfermedad)
admin.site.register(medicamento)
admin.site.register(viaAdministracion)
admin.site.register(horarioAtencion)
admin.site.register(rangoHorario)
admin.site.register(laboratorio)
admin.site.register(solicitudLaboratorio)
admin.site.register(ficha)
admin.site.register(solicitudCita)
admin.site.register(solicitudCitaDetalle)
admin.site.register(especialidad)
admin.site.register(area)
admin.site.register(consultaMedica)
admin.site.register(motivoRechazo)
admin.site.register(tipoMuestra)
admin.site.register(tipoLaboratorio)
admin.site.register(facturaDetalleLaboratorio)
admin.site.register(descuentoArea)
admin.site.register(clienteEnfermedad)
