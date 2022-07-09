from django.urls import path
from contabilidad.views import *

app_name = "contabilidad"
urlpatterns = [
    path('dashboard-contabilidad/', view=dashboardContabilidad.as_view(), name="dashboard-contabilidad"),
    path('facturas/', view=facturas.as_view(), name='facturas'),
    path('pagar-factura/<int:pk>/', view=pagarFactura.as_view(), name='pagar-factura'),
    path('donaciones/', view=donacionesTemplateView.as_view(), name='donaciones'),
    path('crear-donacion/', view=crearDonacionCreateView.as_view(), name='crear-donacion'),
    path('pagos/', view=pagosTemplateView.as_view(), name='pagos'),
    path('pagar-servicio/', view=pagosCreateView.as_view(), name='pagar-servicio')
]
