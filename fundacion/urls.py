from django.urls import path
from fundacion.views import *


app_name = 'fundacion'


urlpatterns = [
    path('dashboard-medico/', view=dashboardMedico.as_view(), name='dashboard-medico'),
    path('crear-consulta/<int:id_expediente>/', view=consultaMedicaCreateView.as_view(), name='crear-consulta'),
    path("crear-tratamiento/<int:solicitud>/",view=tratamientoCreateView.as_view(), name="crear-tratamiento"),
    path("solicitar-laboratorio/<int:solicitud>/",view=laboratorioSolicitudCreate.as_view(), name="solicitar-laboratorio"),
    path("", view=dashboardRecepcion.as_view(), name="dashboard-recepcion"),
    path("crear-laboratorio/<int:id_solicitudLaboratorio>/", view=examenLaboratorioCreateView.as_view(), name="crear-laboratorio"),
    path("actualizar-laboratorio/<int:pk>/", view=editLaboratorioCreateView.as_view(), name="editar-laboratorio"),
    path("actualizar-detalle-solicitud/<int:pk>/", view=solicitudDetalleUpdateDatetimeView.as_view(), name="actualizar-detalle-solicitud"),
    path("rechazar-solicitud-detalle/<int:pk>/", view=rechazarDetalleRechazarView.as_view(), name='rechazar-solicitud-detalle'),
    path("dashboard-laboratorio/", view=dashboardLaboratorio.as_view(), name="dashboard-laboratorio"),
    path("dashboard-farmacia/", view=dashboardFarmacia.as_view(), name="dashboard-farmacia"),
    path("actualizar-tratamiento/<int:pk>/", view=tratamientoUpdateview.as_view(), name="actualizar-tratamiento"),
    path("fichas/", view=fichasListView.as_view(), name="fichas"),
    path("crear-factura/<int:id_ficha>/", view=facturaCrear.as_view(), name="crear-factura"),
    path("facturas/", view=facturasListView.as_view(), name="facturas"),
    path("enfermedad/<int:solicitud>/", view=enfermedadCreateView.as_view(), name="enfermedad")
]   

# <int:id_cliente>/