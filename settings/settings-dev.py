from settings.settings import *

DEBUG=True
ALLOWED_HOSTS = ['*']
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "senes",
        "USER": "sa",
        "PASSWORD": "QWERTYpoiu1231!",
        "HOST": "localhost",
        "PORT": "1433",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
        },
    },
}