from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from asilo.mixins import medicoMixin
from django.urls import reverse
from asilo.models import expediente, contacto
from fundacion.forms import solicitudCitaDetalleForm, solicitudCitaForm
from fundacion.mixins import recepcionMixin
from fundacion.models import solicitudCita, solicitudCitaDetalle
from reportes.correoElectronico import correo
from usuarios.forms import datosPersonalesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.models import datosPersonales
from django.views.generic import TemplateView, CreateView,ListView,  DetailView, DeleteView, UpdateView

# Create your views here.

class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "asilo/home.html"
class dashboardRecepcionView(LoginRequiredMixin,recepcionMixin, TemplateView):
    template_name = "asilo/recepcion/dashboard.html"

    def get(self, request, *args, **kwargs):
        contexto = self.get_contexto()
        return render(request, self.template_name, contexto)
        
class datosPersonalesCreateView(LoginRequiredMixin, CreateView):
    model = datosPersonales
    template_name  = "asilo/includes/forms.html"
    fields = "__all__"
    success_url = ""
    form = datosPersonalesForm()

    def get_context_data(self, **kwargs):
        context = super(datosPersonalesCreateView, self).get_context_data(**kwargs)
        context['titulo'] = "Agregar datos personales"
        return context
        

    def form_valid(self, form):
        form.save()
        _expediente= expediente.objects.create(id_datosPersonales=form.instance)
        print(f"{_expediente.id_expediente}")
        self.success_url= reverse('asilo:contacto', kwargs={'pk':_expediente.id_expediente})
        return super().form_valid(form)

class contactoCreateView(LoginRequiredMixin, CreateView):
    model = contacto
    template_name = "asilo/includes/forms.html"
    fields = ["nombre", "numero_telefono", "correo_electronico", "parentesco"]
    success_url = ""
    
    def get_context_data(self, **kwargs):
        context = super(contactoCreateView, self).get_context_data(**kwargs)
        context['titulo'] = "Agregar datos de contacto"
        return context

    def form_valid(self, form):
        form.instance.id_expediente=expediente.objects.get(id_expediente=self.kwargs['pk'])
        form.save()
        print(self.kwargs['pk'])
        self.success_url = reverse("asilo:expediente", kwargs={'pk':self.kwargs['pk']})
        return super().form_valid(form)

class expedienteDetailView(LoginRequiredMixin, DetailView):
    model = expediente
    template_name = "asilo/recepcion/expediente_detalle.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        _expediente = expediente.objects.get(id_expediente=kwargs['pk'])
        context['expediente'] = _expediente
        context['contacto'] = contacto.objects.filter(id_expediente=_expediente.id_expediente)
        return render(request, self.template_name, context)

class medicoGeneralView(LoginRequiredMixin, TemplateView):
    template_name = "asilo/medico/dashboard.html"

class solicitudCreateView(LoginRequiredMixin, CreateView):
    template_name = "asilo/includes/forms.html"
    model = solicitudCita
    fields = ["id_enfermero", "descripcion"]
    success_url = "/detalle-solicitud/"

    def get(self, request, *args, **kwargs):
        id_expediente = kwargs["id_expediente"]
        form = solicitudCitaForm()
        context = {"form":form}
        solicitud_pendiente, id_solicitud = solicitudCita.get_solicitud(id_expediente=id_expediente)
        if solicitud_pendiente:
            return HttpResponseRedirect(reverse('asilo:detalle-solicitud', kwargs={'id_solicitud':id_solicitud}))
        return render(request, self.template_name, context)

    def form_valid(self, form):
        id_expediente =self.kwargs["id_expediente"]
        _expediente = expediente.objects.get(id_expediente=id_expediente)
        form.instance.id_expediente = _expediente
        form.save()
        self.success_url = self.success_url+ f"{form.instance.id_solicitudCita}/"
        return super().form_valid(form)

class solicitudCitaDetalleCreateView(LoginRequiredMixin,medicoMixin, CreateView):
    template_name = "asilo/medico/crear_solicitud.html"
    model = solicitudCitaDetalle
    fields = ["id_especialidad","descripcion"]
    success_url = "/asilo/dashboard-medico/"
    
    def get(self, request, *args, **kwargs):
        id_solicitud = kwargs["id_solicitud"]
        _solicitud = solicitudCita.objects.get(id_solicitudCita=id_solicitud)
        context = {}
        data = {"id_solicitudCita":_solicitud}
        form = solicitudCitaDetalleForm(initial=data)
        context = {
            "solicitud": _solicitud,
            "form":form,
            "pagina": "detalle"
        }
        detalles = solicitudCitaDetalle.objects.filter(id_solicitudCita=_solicitud)
        if len(detalles) > 0:
            context["detalles"] = detalles
        return render(request, self.template_name, context)

    def form_valid(self, form):
        id_solicitud = self.kwargs["id_solicitud"]
        _solicitud = solicitudCita.objects.get(id_solicitudCita=id_solicitud)
        form.instance.id_solicitudCita = _solicitud
        proximo_paso = self.request.POST["proximo_paso"]
        if proximo_paso =="guardar_y_repetir":
            return HttpResponseRedirect(reverse('asilo:detalle-solicitud', kwargs={'id_solicitud':self.kwargs['id_solicitud']}))
        if proximo_paso =="guardar_y_enviar":
            _solicitudCita= solicitudCita.objects.get(id_solicitudCita=form.instance.id_solicitudCita.id_solicitudCita)
            _solicitudCita.solicitud_finalizada=True
            _solicitudCita.save()
            self.enviar_correo(_solicitudCita)
            return HttpResponseRedirect('/dashboard-medico/')
        

class solicitudDeleteView(LoginRequiredMixin, DeleteView):
    model = solicitudCitaDetalle
    success_url = success_url = "/detalle-solicitud/"
    template_name = "medico/crear_solicitud.html"
    
    def form_valid(self, form):
        # page navegara a finalizar la solicitud
        self.success_url= self.success_url+f"{self.object.id_solicitudCita.id_solicitudCita}/"
        return super().form_valid(form)

class solicitudesListaView(LoginRequiredMixin, ListView):
    template_name = "asilo/medico/solicitudes.html"
    model = solicitudCita

    def get_context_data(self, **kwargs):
        context = super(solicitudesListaView, self).get_context_data(**kwargs)
        context["citas"] = solicitudCita.objects.filter(solicitud_finalizada=False)
        return context