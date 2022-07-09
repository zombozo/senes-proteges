import datetime
from multiprocessing import context
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.contrib import messages
from asilo.models import expediente
from django.urls import reverse
from fundacion.mixins import consultaMedicaMixin, facturaMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  consultaMedicaForm, solicitudCitaDetalleFechaForm, tratamientoForm

from .models import *

# Create your views here.

class dashboardMedico(LoginRequiredMixin, TemplateView):
    template_name = "pages/medico/dashboard_medico.html"
    def get(self, request, *args, **kwargs):
        _solicitudes = solicitudCitaDetalle.objects.filter(id_especialidad__id_area__id_area=1, aceptada=True)
        context = {
            "citas": _solicitudes
        }
        return render(request, self.template_name, context)

class dashboardRecepcion(LoginRequiredMixin, TemplateView):
    template_name = "pages/recepcion/dashboard.html"
    def get(self, request, *args, **kwargs):
        _solicitudes = solicitudCita.objects.filter(solicitud_finalizada=True)
        context = {
            "citas": _solicitudes,
            "form": solicitudCitaDetalleFechaForm()
        }
        return render(request, self.template_name, context)

class dashboardFarmacia(LoginRequiredMixin, TemplateView):
    template_name="pages/dashboard-farmacia.html"

    def get(self, request, *args, **kwargs):
        tratamientos = tratamiento.objects.filter(fecha=datetime.datetime.now())
        context = {
            "tratamientos": tratamientos
        }
        return render(request, self.template_name, context)

class dashboardLaboratorio(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard-laboratorio.html"
    
    def get(self, request, *args, **kwargs):
        citas = solicitudCitaDetalle.objects.filter(id_especialidad__id_area__nombre="Laboratorio", aceptada=True)
        context = {
            "citas": citas
        }
        return render(request, self.template_name, context)

class examenLaboratorioCreateView(LoginRequiredMixin, CreateView):
    template_name = "pages/dashboard-laboratorio.html"
    model = laboratorio
    fields = ["tipo_muestra","resultado", "descripcion_resultado"]
    success_url = ""
    
    def get_success_url(self):
        return reverse("fundacion:dashboard-laboratorio")
    
    def get_context_data(self, **kwargs):
        context = super(examenLaboratorioCreateView, self).get_context_data(**kwargs)
        context["titulo"] = "Examen de laboratorio"
        context["detalle"] = solicitudCitaDetalle.objects.get(solicitudCitaDetalle=self.kwargs['id_solicitudDetalle'])
        return context
        
    
    def form_valid(self, form):
        id_solicitudCitaDetalle = solicitudCitaDetalle.objects.get(solicitudCitaDetalle=self.kwargs["id_solicitudDetalle"])
        form.instance.id_solicitudCitaDetalle = id_solicitudCitaDetalle
        form.instance.id_ficha = ficha.get_ficha(_solicitudCitaDetalle=id_solicitudCitaDetalle)
        form.save()
        facturaDetalleEspecialidad.save_factura_detalle(form.instance)
        return super().form_valid(form)

class editLaboratorioCreateView(LoginRequiredMixin, UpdateView):
    model = laboratorio
    template_name = "pages/dashboard-laboratorio.html"
    fields = ["resultado", "descripcion_resultado", "finalizado"]
    success_url= "/fundacion/dashboard-laboratorio/"

    def form_valid(self, form):
        if form.instance.resultado !="" or form.instance.resultado != None:
            form.finalizado=True
        return super(editLaboratorioCreateView, self).form_valid(form)
    
class consultaMedicaCreateView(LoginRequiredMixin,consultaMedicaMixin, CreateView):
    model = consultaMedica
    fields = ["diagnostico"]
    template_name = "pages/medico/consulta_crear.html"
    success_url = ""


    def get_success_url(self):
        return reverse("fundacion:dashboard-medico")

    def get(self, request, *args, **kwargs):
        context = self.get_contexto()
        return render(request, self.template_name, context)
        
    def form_valid(self, form):
        id_detalle = self.request.GET.get("detalle")
        
        detalle=solicitudCitaDetalle.objects.get(solicitudCitaDetalle=id_detalle)
        _ficha = ficha.get_ficha(_solicitudCitaDetalle=detalle)
        form.instance.id_solicitudCitaDetalle=detalle
        form.instance.id_ficha = _ficha
        form.save()
        facturaDetalleEspecialidad.save_factura_detalle(form.instance)
        return super().form_valid(form)

class tratamientoCreateView(LoginRequiredMixin, CreateView):
    template_name = "pages/medico/consulta_crear.html"
    success_url = "/crear-consulta/"
    fields = ["medicamento", "cantidad","descripcion"]
    model = tratamiento
    # tratamientoForm
    def get(self, request, *args, **kwargs):
        id_solicitud = kwargs["solicitud"]
        solicitud = solicitudCitaDetalle.objects.get(solicitudCitaDetalle=id_solicitud)

        form  = tratamientoForm()
        context= {
            "form":form,
            "solicitud_detalle":solicitud
        }

        return render(request, self.template_name, context)
    
    
    def form_valid(self, form, **kwargs):
        id_solicitud = self.kwargs["solicitud"]
        solicitud = solicitudCitaDetalle.objects.get(solicitudCitaDetalle=id_solicitud)
        form.instance.id_ficha = ficha.get_ficha(_solicitudCitaDetalle=solicitud)
        self.success_url = self.success_url+f"{solicitud.id_solicitudCita.id_expediente.id_expediente}/?detalle={solicitud.solicitudCitaDetalle}"
        return super().form_valid(form)
    
class tratamientoUpdateview(LoginRequiredMixin, UpdateView):
    model = tratamiento
    fields = ["estado", "cantidad"]
    success_url= ""

    def get_success_url(self):
        return reverse("fundacion:dashboard-farmacia")
    
    def form_valid(self, form):
        form.save()
        facturaDetalleFarmacia.set_detalleFactura(form.instance)
        return super(tratamientoUpdateview, self).form_valid(form)
    
class solicitudDetalleUpdateDatetimeView(LoginRequiredMixin, UpdateView):
    template_name="pages/recepcion/dashboard.html"
    model = solicitudCitaDetalle
    fields = ["fecha_hora"]
    def post(self, request, *args, **kwargs) :
        data_time = request.POST.getlist('fecha_hora')
        str_datetime = f"{data_time[0]} {data_time[1]}"
        print(f"{str_datetime}")
        _datetime = datetime.datetime.strptime(str_datetime,"%Y-%m-%d %H:%M")
        data = {"fecha_hora":_datetime}
        form = solicitudCitaDetalleFechaForm(data=data)
        if form.is_valid():
            _solicitudCitaDetalle=solicitudCitaDetalle.objects.get(solicitudCitaDetalle=kwargs['pk'])
            _solicitudCitaDetalle.fecha_hora = form.cleaned_data["fecha_hora"]
            _solicitudCitaDetalle.aceptada=True
            _solicitudCitaDetalle.save()
        else:
            print(f"errores: {form.errors}")
            messages.error(request, form.errors)
        return redirect('/fundacion')

class rechazarDetalleRechazarView(LoginRequiredMixin, CreateView):
    template_name = "pages/recepcion/dashboard.html"
    model = motivoRechazo
    fields = ["motivo"]
    def form_valid(self, form) :
        detalle =solicitudCitaDetalle.objects.get(solicitudCitaDetalle=self.kwargs['pk'])
        form.instance.id_solicitudCitaDetalle = detalle
        form.save()
        
        detalle.aceptada=False
        detalle.save()
        return HttpResponseRedirect(reverse("fundacion:dashboard-recepcion"))

class fichasListView(LoginRequiredMixin, ListView):
    template_name = "pages/recepcion/fichas.html"
    model = ficha
    
    def get(self, request, *args, **kwargs):
        fichas = ficha.objects.all()
        context = {
            "fichas":fichas
        }
        return render(request, self.template_name,context )

class facturaCrear(LoginRequiredMixin, facturaMixin, CreateView):
    template_name = "pages/recepcion/generar_factura.html"
    model = factura
    fields = ["direccion", "nit"]
    success_url = ""

    def get_absolute_url(self):
        return reverse("fundacion:fichas")
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(facturaCrear, self).get_context_data(*args, **kwargs)
        context["ficha"] = ficha.objects.get(id_ficha=self.kwargs['id_ficha'])
        return context

    def form_valid(self, form) -> HttpResponse:
        form.instance.id_ficha = ficha.objects.get(id_ficha=self.kwargs['id_ficha'])
        form.save()
        self.crear_detalle(form.instance.id_factura, self.kwargs['id_ficha'])
        return super().form_valid(form)