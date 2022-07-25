
import os
from pathlib import Path
import concurrent.futures
from posixpath import abspath
import subprocess
import os
from os.path import abspath
import time


from django.conf import settings

from reportes.controlErrores import get_loggerSenes

class backups:
    
    def __init__(self) -> None:
        self.rutaBackup=os.path.join(settings.BASE_DIR,'backups')
    def execCommandBackup(self):
        return subprocess.run(["sh",f"{self.rutaBackup}/crear_backup_command.sh" ], capture_output=True)
    
    def createBackup(self):
        logger=get_loggerSenes()
        ruta = Path(__file__).resolve().parent
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future = executor.submit(self.execCommandBackup, )
            processCompleted = future.result()
            logger.info(processCompleted.stdout)
            string_data = processCompleted.stdout
            string_data = string_data.decode()
            results = string_data.split("\n")
            results.pop()
            last = results.pop()
            if "BACKUP DATABASE successfully" in last:
                return {"status":True, "message":"Backup de base de datos, realizado!"}
            else:
                return {"status":False, "message":"Error, no se pudo realizar el backup, intente de nuevo!"}
    def eliminar_backups(self, nombre):
        if os.path.exists(f"{self.rutaBackup}/{nombre}"):
            os.remove(f"{self.rutaBackup}/{nombre}")
            return {"status":True, "message":f"Eliminado el backup {nombre}"}
        else:
            return {"status":False, "message":"No se encontro el archivo"}
    
    def get_backupsExistentes(self):
        lista = []
        for archivo in os.scandir(self.rutaBackup):
            backup = dict()
            if archivo.is_file():
                ruta=abspath(archivo.path)
                list_ruta=ruta.split("/")
                nombre=list_ruta[-1]
                nombre_lista = nombre.split(".")
                if nombre_lista[-1] == "bak":
                    backup["ruta"]=ruta
                    backup["nombre"]=nombre
                    backup["fecha"]=time.ctime(os.path.getctime(ruta))
                    lista.append(backup)
        return lista
    
    
    def get_bak(self, nombre):
        ruta = f"{self.rutaBackup}/{nombre}"
        return open(ruta, 'rb')