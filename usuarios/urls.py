

from django.urls import path

from usuarios.views import expedienteSearch

app_name= "usuarios"
urlpatterns = [
    path("buscar-expediente/", view=expedienteSearch.as_view(), name="buscar-expediente")
]
