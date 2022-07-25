password de mssql-server:
Qwerty123!@#


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

docker run -d -p 1433:1433  -v /home/ubuntu/senes-proteges/backups:/var/opt/mssql/data/backups --name mssqlserverV2 mssqlserver-bak