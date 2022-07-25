# ![senes-proteges](/static/imagenes/grasshopperIcon.png) Senes proteges # ![senes-proteges](/static/imagenes/grasshopperIcon.png)
senes-salutem-proteges - hogar para ancianos



Es un proyecto pensado para gestionar las actividades del asilo Nueva vida y proporcinara usuarios de acceso a los empleados de la fundacion buena vida, para que desde su lugar de trabajo, alimenten el expediente del residente del asilo, cada ves que este realice una visita medica.

esto permitira un mejor control del estado de salud de los residentes.

Visite la seccion [WIKI](https://github.com/zombozo/senes-proteges/wiki) de este repositorio para conocer todos los detalles del proyecto.

Ademas puede visitar cada issue en la seccion de [ZENHUB](https://github.com/zombozo/senes-proteges/wiki#workspaces/senes-proteges-62b5c7814d85c1001a6af6b9/board?repos=496660399) para conocer la documentacion  y el proceso implementado para el desarrollo de este proyecto.


## Como instalar en su entorno local
> clone el proyecto desde este repositorio
```
git clone https://github.com/zombozo/senes-proteges.git
```

> Accede a la carpeta donde se creo la copia y cree un entorno local python con los comandos:
```
  cd senes-proteges
  python3 -m venv venv
  
```
> Acceda al entorno virtual python que ha creado e instale las dependencias del proyecto
###### ubuntu 
```
source venv/bin/activate
```
###### windows

```
pip install virtualenv
vitualenv venv
```

una ves dentro del entorno virtual instale las dependencias del proyecto

```
  pip install -r requirements.txt
```



# configuracion del servidor web senes proteges


## ejecutar docker con mssql server 

Start a mssql-server instance running as the SQL Express edition
```
docker run -d -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=****" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=*****" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
start 
```
