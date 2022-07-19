
from asilo.herramientas import backups
from rest_framework.views import APIView
from rest_framework.response import Response


class BackupsDB(APIView):
    
    def get(self, request, *args, **kwargs):
        back = backups()
        back.createBackup()
        return Response("Ejecutado")
    