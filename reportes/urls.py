from .views import *
from django.urls import path


app_name = "reportes"
urlpatterns = [
    path("fichas/", view=fichasView.as_view(), name="fichas"),
    path("medicos/", view=medicoView.as_view(), name="medicos"),
    path("cobros/", view=cobrosView.as_view(), name="cobros"),
    path("pagos/", view=pagosView.as_view(), name="pagos"),
    path("donaciones/", view=donacionesView.as_view(), name="donaciones"),
    path("medicamentos/", view=medicamentosView.as_view(), name="medicamentos"),
]
