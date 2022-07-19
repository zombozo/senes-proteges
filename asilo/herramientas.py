
import os
from pathlib import Path
import concurrent.futures
import subprocess


from django.conf import settings

from reportes.controlErrores import get_loggerSenes

class backups:
    
    def __init__(self) -> None:
        self.rutaBackup=os.path.join(settings.BASE_DIR,'backups')
        self.commandforbackup=f"BACKUP DATABASE senes TO DISK='{self.rutaBackup}/senes.bak'"
        self.host='localhost'
        self.user="sa"
        self.passwd='Qwerty123!@#'
        
    def execCommandBackup(self):
        return subprocess.run(["sqlcmd", "-U", self.user, "-P", self.passwd,"-S",self.host, "-Q", self.commandforbackup], capture_output=True)
    
    def createBackup(self):
        logger=get_loggerSenes()
        ruta = Path(__file__).resolve().parent
        print(f"----> {ruta}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future = executor.submit(self.execCommandBackup, )
            processCompleted = future.result()
            logger.info(processCompleted.stdout)
    