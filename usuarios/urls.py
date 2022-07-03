from django.contrib.auth.views import LogoutView

from django.urls import path

from usuarios.views import AdminLogin, expedienteSearch

app_name= "usuarios"
urlpatterns = [
    path("buscar-expediente/", view=expedienteSearch.as_view(), name="buscar-expediente"),
    path("iniciar-sesion/",view=AdminLogin.as_view(), name="iniciar-sesion"),
    path("logout/", LogoutView.as_view(), name="logout")
]
