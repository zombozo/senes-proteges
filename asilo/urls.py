
from django.urls import path
from .views import *

app_name= "asilo"
urlpatterns = [
    path("",view=HomeTemplateView.as_view(), name="home"),
    path("recepcion/", view=dashboardRecepcionView.as_view(), name="dashboard-recepcion"),
    path('datos-personales/',view=datosPersonalesCreateView.as_view(), name="datos-personales"),
    path('contacto/<int:pk>/', view=contactoCreateView.as_view(), name="contacto"),
    path('expediente/<int:pk>/', view=expedienteDetailView.as_view(), name="expediente"),
    path("dashboard-medico/", view=medicoGeneralView.as_view(), name="dashboard-medico"),
    path("crear-solicitud/<int:id_expediente>/", view=solicitudCreateView.as_view(), name="crear-solicitud"),
    path("detalle-solicitud/<int:id_solicitud>/",  view=solicitudCitaDetalleCreateView.as_view(), name="detalle-solicitud"),
    path("eliminar-detalle-solicitud/<int:pk>/", view=solicitudDeleteView.as_view(), name="eliminar-detalle-solicitud"),
    path("lista-solicitudes/", view=solicitudesListaView.as_view(), name="lista-solicitudes"),
]
