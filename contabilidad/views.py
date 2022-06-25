from django.shortcuts import render
from django.views.generic import TemplateView

from asilo.models import cuenta, expediente
from fundacion.models import factura



# Create your views here.
class dashboardContabilidad(TemplateView):
    template_name="contabilidad/home-contabilidad.html"
    def get(self, request, *args, **kwargs):
        expedientes = expediente.objects.all()
        facturas = factura.objects.all()
        print(facturas)
        context = {
            "expedientes":expedientes,
            "facturas": facturas
        }
        return render(request, self.template_name, context)