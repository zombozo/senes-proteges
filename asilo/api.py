
from django.http import JsonResponse
from asilo.herramientas import backups
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

from fundacion.models import solicitudCitaDetalle



class BackupsDB(APIView):
    
    def get(self, request, *args, **kwargs):
        back = backups()
        result = back.createBackup()
        return Response(result)
    
    @api_view(('GET',))
    def eliminar_backup(self, nombre):
        back = backups()
        return Response(back.eliminar_backups(nombre))
    
    
class ver_detalle_solicitud(APIView):
    def get(self, request, *args, **kwargs):
        id_solicitud = kwargs["solicitud"]
        detalle = list(solicitudCitaDetalle.objects.filter(id_solicitudCita=id_solicitud).values('id_empleado__id_datos_personales__primer_nombre','id_empleado__id_datos_personales__primer_apellido', 'id_especialidad__especialidad','descripcion', 'fecha_hora', 'aceptada'))
        return JsonResponse(detalle, safe=False)