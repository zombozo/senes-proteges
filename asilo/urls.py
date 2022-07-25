
from django.urls import path

from asilo.api import BackupsDB, ver_detalle_solicitud
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
    path("editar-solicitud/<int:pk>/", view=solicitudCitaDetalleUpdateView.as_view(), name="editar-solicitud"),
    path("crear-backup/", view=BackupsDB.as_view(), name="crear-backup"),
    path("configuraciones/", view=configuracionesView.as_view(), name="configuraciones"),
    path("descargar/<str:nombre>/", view=configuracionesView.descargar_bak, name="descargar"),
    path("eliminar-backup/<str:nombre>/", view=BackupsDB.eliminar_backup, name="eliminar-backup"),
    path("ver-detalle-solicitud/<int:solicitud>/", view=ver_detalle_solicitud.as_view(), name="ver-detalle-solicitud"),
]
