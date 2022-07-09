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
docker run -d -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Qwerty123!@#" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Qwerty123!@#" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
start 
```
sudo docker start 10fd092898b2 #server 97d3be24d811

Connect to Microsoft SQL Server You can connect to the SQL Server using the sqlcmd tool inside of the container by using the following command on the host:
```
docker exec -it 10fd092898b2 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Qwerty123!@#
97d3be24d811
sudo docker exec -it 97d3be24d811 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'Qwerty123!@#'
```
### conectarse a sqlserver via sqlcmd sin docker
```
sqlcmd -S localhost -U sa -P 'Qwerty123!@#'

```

### las siguientes dependencias son necesarias
```
sudo apt install python3-pip python3-dev libpq-dev   nginx 
pip install  gunicorn psycopg2-binary
```

### Solucionar problemas de gunicorn

```
sudo systemctl status gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```


### acceso a la configuracion del servidor 
```
sudo nano /etc/nginx/sites-available/myproject

sudo ln -s /etc/nginx/sites-available/senes-proteges /etc/nginx/sites-enabled 


/etc/nginx/sites-enabled
 ```


###  ruta del archvivo de configuracion de gunicorn 
```
/etc/systemd/system/gunicorn.service

/etc/nginx/sites-available/ #/etc/nginx/sites-enabled
```


sudo systemctl restart nginx

### verificar el log de gunicorn
```
sudo journalctl -u gunicorn.socket

```