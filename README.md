# senes-proteges
senes-salutem-proteges - hogar para ancianos

Es un proyecto pensado para gestionar las actividades del asilo Nueva vida y proporcinara usuarios de acceso a los empleados de la fundacion buena vida, para que desde su lugar de trabajo, alimenten el expediente del residente del asilo, cada ves que este realice una visita medica.

esto permitira un mejor control del estado de salud de los residentes.

Visite la seccion WIKI de este repositorio para conocer todos los detalles del proyecto.

Ademas puede visitar cada issue en la seccion de ZENHUB para conocer la documentacion  y el proceso implementado para el desarrollo de este proyecto.

# configuracion del servidor web senes proteges


## ejecutar docker con mssql server 

Start a mssql-server instance running as the SQL Express edition
```
docker run -d -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=****" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=*****" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
start 
```
