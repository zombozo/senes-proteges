from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from contabilidad.models import cobro, donacion, pago

from fundacion.models import consultaMedica, factura, tratamiento
from reportes.mixins import reporteMixin

# Create your views here.
class fichasView(LoginRequiredMixin,reporteMixin, TemplateView ):
    template_name = "reportes/includes/fichas.html"
    
    def get(self,request, **kwargs):
        context = {}
        if request.GET.get("cliente"): # DPI
            context["facturas"] = self.get_factura_by_usuario(request.GET.get("cliente"), int(self.request.GET.get("opcion")))
        elif request.GET.get("dateInit"): #date
            context["facturas"] = self.get_factura_by_date(request.GET.get("dateInit"), request.GET.get("dateFin"))
        else:
            context["facturas"] =factura.objects.all()
        return render(request, self.template_name, context)

class medicoView(LoginRequiredMixin, reporteMixin, TemplateView):
    template_name = "reportes/includes/consultasMedicas.html"
    def get(self, request, **kwargs):
        context = {}
        if request.GET.get("cliente"): # DPI
            context["consultas"] = self.get_consultas_by_cliente(request.GET.get("cliente"), int(self.request.GET.get("opcion")))
        elif request.GET.get("dateInit"): #date
            context["consultas"]= self.get_consultas_by_date(request.GET.get("dateInit"), request.GET.get("dateFin"))
        else:
            context["consultas"]=consultaMedica.objects.all()
        return render(request, self.template_name, context)
    
class cobrosView(LoginRequiredMixin, reporteMixin, TemplateView):
    template_name = "reportes/includes/cobros.html"
    def get(self, request, **kwargs):
        context = {}
        if request.GET.get("cliente"): # DPI
            context["facturas"] = self.get_cobro_by_usuario(int(request.GET.get("cliente")), int(self.request.GET.get("value")))
            print(f"contexto en cliente: {context}")
        elif request.GET.get("dateInit"): #date
            context["facturas"] = self.get_cobro_by_date(request.GET.get("dateInit"), request.GET.get("dateFin"))
            print(f"contexto en fecha: {context}")
        else:
            context["facturas"]=self.get_cobro()
            print(f"contexto sin dato: {context}")
        return render(request, self.template_name, context)
    
class pagosView(LoginRequiredMixin, reporteMixin, TemplateView):
    template_name = "reportes/includes/pagos.html"
    def get(self, request, **kwargs):
        
        context = {}
        if  request.GET.get("dateInit"):
            context["pagos"]=self.get_pagos_by_date(request.GET.get("dateInit"), request.GET.get("dateFin"))
        
        elif request.GET.get("nombre"):
            context["pagos"] = self.get_pagos_by_nombre_servicio(request.GET.get("nombre"))
        else:
            context["pagos"]=pago.objects.all()
        return render(request, self.template_name, context)

class donacionesView(LoginRequiredMixin, reporteMixin, TemplateView):
    template_name = "reportes/includes/donaciones.html"
    def get(self, request, **kwargs):
        context = {}
        if request.GET.get("dateInit"):
            context["donaciones"]= self.get_donaciones_by_fecha(request.GET.get("dateInit"), request.GET.get("dateFin"));
            
        elif request.GET.get("donante"):
            context["donaciones"]=self.get_donaciones_by_donante(request.GET.get("donante"))
        else:
            context["donaciones"]=donacion.objects.all()[:10]
        return render(request, self.template_name, context)

class medicamentosView(LoginRequiredMixin, reporteMixin, TemplateView):
    template_name = "reportes/includes/medicamentos.html"
    def get(self, request, **kwargs):
        
        context = {}
        if request.GET.get("cliente"):
            context["tratamientos"]=self.get_medicamentos_by_cliente(request.GET.get("cliente"), request.GET.get("opcion"))
        elif request.GET.get("dateInit"):
            context["tratamientos"]=self.get_medicamentos_by_date(request.GET.get("dateInit"), request.GET.get("dateFin"))
        else:
            context["tratamientos"]=tratamiento.objects.all()
        return render(request, self.template_name, context)