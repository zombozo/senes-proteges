

from django.urls import path

from fundacion.views import *


app_name = 'fundacion'


urlpatterns = [
    path('dashboard-medico/', view=dashboardMedico.as_view(), name='dashboard-medico'),
    path('crear-consulta/<int:id_expediente>/', view=consultaMedicaCreateView.as_view(), name='crear-consulta'),
    path("crear-tratamiento/<int:solicitud>/",view=tratamientoCreateView.as_view(), name="crear-tratamiento"),
    path("", view=dashboardRecepcion.as_view(), name="dashboard-recepcion"),
    path("crear-laboratorio/<int:id_solicitudDetalle>/", view=examenLaboratorioCreateView.as_view(), name="crear-laboratorio"),
    path("actualizar-detalle-solicitud/<int:pk>/", view=solicitudDetalleUpdateDatetimeView.as_view(), name="actualizar-detalle-solicitud"),
    path("actualizar-solicitud-cita/<int:pk>/", view=solicitudUpdateView.as_view(), name='actualizar-solicitud-cita'),
    path("dashboard-laboratorio/", view=dashboardLaboratorio.as_view(), name="dashboard-laboratorio"),
    path("dashboard-farmacia/", view=dashboardFarmacia.as_view(), name="dashboard-farmacia"),
    path("actualizar-tratamiento/<int:pk>/", view=tratamientoUpdateview.as_view(), name="actualizar-tratamiento")
]

# <int:id_cliente>/