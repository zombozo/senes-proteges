from django.conf import settings
from django.shortcuts import render
from asilo.models import expediente, contacto
from fundacion.forms import solicitudCitaDetalleForm, solicitudCitaForm
from fundacion.models import solicitudCita, solicitudCitaDetalle
from reportes.correoElectronico import correo
from usuarios.forms import datosPersonalesForm

from usuarios.models import datosPersonales
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView

# Create your views here.
class dashboardRecepcionView(TemplateView):
    template_name = "recepcion/dashboard.html"

class datosPersonalesCreateView(CreateView):
    model = datosPersonales
    template_name  = "includes/forms.html"
    fields = "__all__"
    success_url = "/contacto/"
    form = datosPersonalesForm()

    def form_valid(self, form):
        form.save()
        expediente.objects.create(id_datosPersonales=form.instance)
        self.success_url= self.success_url + f"{form.instance.id_datosPersonales}/"
        return super().form_valid(form)

class contactoCreateView(CreateView):
    model = contacto
    template_name = "includes/forms.html"
    fields = "__all__"
    success_url = "/expediente/"

    def form_valid(self, form):
        form.save()
        print(self.kwargs)
        self.success_url = self.success_url+f"{self.kwargs['pk']}/"
        return super().form_valid(form)

class expedienteDetailView(DetailView):
    model = expediente
    template_name = "recepcion/expediente_detalle.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        _expediente = expediente.objects.get(id_expediente=kwargs['pk'])
        context['expediente'] = _expediente
        context['contacto'] = contacto.objects.get(id_expediente=_expediente)
        return render(request, self.template_name, context)

class medicoGeneralView(TemplateView):
    template_name = "medico/dashboard.html"

class solicitudCreateView(CreateView):
    template_name = "includes/forms.html"
    model = solicitudCita
    fields = ["id_enfermero", "descripcion"]
    success_url = "/asilo/detalle-solicitud/"

    def get(self, request, *args, **kwargs):
        id_expediente = kwargs["id_expediente"]
        form = solicitudCitaForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def form_valid(self, form):
        id_expediente =self.kwargs["id_expediente"]
        _expediente = expediente.objects.get(id_expediente=id_expediente)
        form.instance.id_expediente = _expediente
        form.save()
        self.success_url = self.success_url+ f"{form.instance.id_solicitudCita}/"
        return super().form_valid(form)

class solicitudCitaDetalleCreateView(CreateView):
    template_name = "medico/crear_solicitud.html"
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
            self.success_url = f"/asilo/detalle-solicitud/{self.kwargs['id_solicitud']}/"
        if proximo_paso =="guardar_y_enviar":
            _solicitudCita= solicitudCita.objects.get(id_solicitudCita=form.instance.id_solicitudCita.id_solicitudCita)
            _solicitudCita.solicitud_finalizada=True
            _solicitudCita.save()
            _correo = correo()
            contenido = {}
            _correo.set_contenidoCorreo(
                destinatario=settings.EMAIL_HOST_USER,
                subject="Test",
                contexto=contenido,
                to=["weowulft02@gmail.com"]
            )
            _correo.enviar(contexto=contenido)
        
        return super().form_valid(form)

class solicitudDeleteView(DeleteView):
    model = solicitudCitaDetalle
    success_url = success_url = "/asilo/detalle-solicitud/"
    template_name = "medico/crear_solicitud.html"
    
    def form_valid(self, form):
        # page navegara a finalizar la solicitud
        self.success_url= self.success_url+f"{self.object.id_solicitudCita.id_solicitudCita}/"
        return super().form_valid(form)

