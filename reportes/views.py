from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from contabilidad.models import cobro, donacion, pago

from fundacion.models import consultaMedica, factura, tratamiento
from reportes.mixins import reporteMixin

# Create your views here.
class fichasView(LoginRequiredMixin, TemplateView ):
    template_name = "reportes/includes/fichas.html"
    
    def get(self,request, **kwargs):
        _factura = factura.objects.all()
        context = {}
        context["facturas"] =_factura
        return render(request, self.template_name, context)

class medicoView(LoginRequiredMixin, TemplateView):
    template_name = "reportes/includes/consultasMedicas.html"
    def get(self, request, **kwargs):
        
        context = {}
        context["consultas"]=consultaMedica.objects.all()
        return render(request, self.template_name, context)
    
class cobrosView(LoginRequiredMixin, reporteMixin, TemplateView):
    template_name = "reportes/includes/cobros.html"
    def get(self, request, **kwargs):
        context = {}
        if request.GET.get("cliente"): # DPI
            context["facturas"] = self.get_cobro_by_usuario(int(request.GET.get("cliente")), int(self.request.GET.get("value")))
        if request.GET.get("dateInit"): #date
            context["facturas"] = self.get_cobro_by_date(request.GET.get("dateInit"), request.GET.get("dateFin"))
        context["facturas"]=self.get_cobro()
        return render(request, self.template_name, context)
    
class pagosView(LoginRequiredMixin, TemplateView):
    template_name = "reportes/includes/pagos.html"
    def get(self, request, **kwargs):
        
        context = {}
        context["pagos"]=pago.objects.all()
        return render(request, self.template_name, context)

class donacionesView(LoginRequiredMixin, TemplateView):
    template_name = "reportes/includes/donaciones.html"
    def get(self, request, **kwargs):
        context = {}
        context["donaciones"]=donacion.objects.all()
        return render(request, self.template_name, context)

class medicamentosView(LoginRequiredMixin, TemplateView):
    template_name = "reportes/includes/medicamentos.html"
    def get(self, request, **kwargs):
        
        context = {}
        context["tratamientos"]=tratamiento.objects.all()
        return render(request, self.template_name, context)