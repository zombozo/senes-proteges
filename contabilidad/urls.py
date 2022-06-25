from django.urls import path
from contabilidad.views import dashboardContabilidad

app_name = "contabilidad"
urlpatterns = [
    path('dashboard-contabilidad/', view=dashboardContabilidad.as_view(), name="dashboard-contabilidad")
]
