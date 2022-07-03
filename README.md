# senes-proteges
senes-salutem-proteges - hogar para ancianos



## ejecutar docker para mssql server 

Start a mssql-server instance running as the SQL Express edition

docker run -d -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Qwerty123!@#" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Qwerty123!@#" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest
start 

sudo docker start 10fd092898b2 #server 97d3be24d811

Connect to Microsoft SQL Server You can connect to the SQL Server using the sqlcmd tool inside of the container by using the following command on the host:

docker exec -it 10fd092898b2 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Qwerty123!@#
97d3be24d811
sudo docker exec -it 97d3be24d811 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'Qwerty123!@#'

conectarse a sqlserver 

sqlcmd -S localhost -U sa -P 'Qwerty123!@#'
sudo apt install python3-pip python3-dev libpq-dev   nginx 
pip install  gunicorn psycopg2-binary


## Solucionar problemas de gunicorn

sudo systemctl status gunicorn.socket
    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn



# acceso a la configuracion del servidor 
sudo nano /etc/nginx/sites-available/myproject

sudo ln -s /etc/nginx/sites-available/senes-proteges /etc/nginx/sites-enabled

sites-availablsenes-protegesct

 /etc/nginx/sites-enabled


#  ruta del archvivo de configuracion de ginicorn /etc/systemd/system/gunicorn.service

# /etc/nginx/sites-available/ #/etc/nginx/sites-enabled