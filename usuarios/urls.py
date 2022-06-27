

from django.urls import path

from usuarios.views import AdminLogin, expedienteSearch

app_name= "usuarios"
urlpatterns = [
    path("buscar-expediente/", view=expedienteSearch.as_view(), name="buscar-expediente"),
    path("iniciar-sesion/",view=AdminLogin.as_view(), name="iniciar-sesion")
]
