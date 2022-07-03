from settings.settings import *

DEBUG=True
ALLOWED_HOSTS = ['18.216.38.243']
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "senes",
        "USER": "sa",
        "PASSWORD": "Qwerty123!@#",
        "HOST": "localhost",
        "PORT": "1433",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
        },
    },
}