from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from asilo.models import cuenta, expediente
from fundacion.models import factura
from django.contrib import messages
from .models import *
from . import mixins
from .forms import *


# Create your views here.
class dashboardContabilidad(LoginRequiredMixin, TemplateView):
    template_name="contabilidad/home-contabilidad.html"
    def get(self, request, *args, **kwargs):
        expedientes = expediente.objects.all()
        facturas = factura.objects.all()
        context = {
            "expedientes":expedientes,
            "facturas": facturas
        }

        return render(request, self.template_name, context)
        
class facturas(LoginRequiredMixin, TemplateView):
    template_name = 'contabilidad/includes/facturas.html'
    
    def get(self,request, **kwargs):
        _factura = factura.objects.all()
        context = {}
        context["facturas"] =_factura
        return render(request, self.template_name, context)

class pagarFactura(LoginRequiredMixin, mixins.contabilidadMixin, CreateView):
    model = transaccion
    template_name = 'contabilidad/includes/facturas.html'
    success_url = '/contabilidad/dashboard-contabilidad/'
    fields = ["monto"]
    
    def get_context_data(self, **kwargs):
        context = super(pagarFactura, self).get_context_data(**kwargs)
        id_factura = self.kwargs['pk']
        _factura = factura.objects.get(id_factura=id_factura)
        context["factura"] =_factura
        context["total"] = self.get_total(_factura)
        return context
    
    def form_valid(self, form):
        form.save()
        cobro.set_cobro(form.instance, self.kwargs['pk'])
        messages.success(self.request, "Pago realizado correctamente!")
        return super().form_valid(form)

class donacionesTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "contabilidad/includes/donaciones.html"


    def get(self, request, *args, **kwargs):
        donaciones = donacion.objects.all()
        contexto = {}
        contexto["donaciones"] = donaciones
        print(contexto)
        return render(request, self.template_name, contexto)
        
class crearDonacionCreateView(LoginRequiredMixin, TemplateView):
    template_name = "contabilidad/includes/donaciones.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            "form":donacionForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        monto = request.POST.get("monto")
        form = donacionForm(request.POST)
        if form.is_valid():
            _transaccion = transaccion.objects.create(monto=monto)
            form.instance.id_transaccion = _transaccion
            form.save()
            messages.success(self.request, f"Nueva donacion creada con exito!, {form.instance.nombre} Q.{_transaccion.monto}")
            return HttpResponseRedirect('/contabilidad/donaciones/')
        else:
            context = {}
            context["form"] = form
            messages.error(self.request, "Algunos elementos no son correctos! intente de nuevo.")
            return render(request, self.template_name, context)
        return HttpResponseRedirect('/contabilidad/donaciones/')

class pagosTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "contabilidad/includes/pagos.html"

    def get(self, request, *args, **kwargs):
        pagos = pago.objects.all()
        context = {
            "pagos":pagos,
            "paginaPagos":1
        }
        print(context)
        return render(request, self.template_name, context)

class pagosCreateView(LoginRequiredMixin, CreateView):
    model = pago
    template_name = "contabilidad/includes/pagos.html"
    success_url = "/contabilidad/pagos"
    fields = ["id_servicio"]

    def get(self, request, *args, **kwargs):
        context = {
            "form":pagosForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        monto = request.POST.get("monto")
        form = pagosForm(request.POST)
        if form.is_valid():
            _transaccion = transaccion.objects.create(monto=monto)
            form.instance.id_transaccion = _transaccion
            form.save()
            messages.success(self.request, f"Servicio pagado correctamente, {form.instance.id_servicio.nombre} por Q.{_transaccion.monto}")
        else:
            return render(request, self.template_name, {"form":form})

        return HttpResponseRedirect("/contabilidad/pagos/")



 