# senes-proteges
senes-salutem-proteges - hogar para ancianos



## ejecutar docker para mssql server 

Start a mssql-server instance running as the SQL Express edition

docker run -d -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=QWERTYpoiu1231!" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest

start 

sudo docker start 10fd092898b2

Connect to Microsoft SQL Server You can connect to the SQL Server using the sqlcmd tool inside of the container by using the following command on the host:

docker exec -it 10fd092898b2 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P QWERTYpoiu1231!
