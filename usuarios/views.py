from audioop import reverse
from curses.ascii import NUL
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from notifications.signals import notify
from django.contrib import messages

from asilo.models import expediente
from asilo.views import HomeTemplateView, dashboardRecepcionView
from usuarios.models import empleado

# Create your views here.

class expedienteSearch(ListView):
    model = expediente
    template_name= "buscar.html"
    
    def get(self, request, *args, **kwargs):
        opcion = request.GET.get("opcion")
        search = request.GET.get("search")
        expedientes = {}
        if opcion == "1":
            try:
                _search = int(search)
                expedientes = expediente.objects.filter(id_datosPersonales__dni=_search)
            except ValueError as e:
                messages.debug(request, "los parametros ingresados no son un Numero de DPI valido, intente ingresando solo numeros! ")
        if opcion == "2":
            expedientes = expediente.objects.filter(id_datosPersonales__primer_nombre__startswith=search )
        if opcion == "3":
            expedientes = expediente.objects.filter(id_datosPersonales__primer_apellido__startswith=search)
        if opcion == "4":
            expedientes = expediente.objects.filter(codigo_expediente__startswith=search)
        context = {
            "expedientes": expedientes
        }
        return render(request, self.template_name, context)
        
class AdminLogin(LoginView):
    template_name = "usuarios/iniciar-sesion.html"
    success_url  = '/'
    
    def get_success_url(self) -> str:
        print("Usuario logeado exitosamente")
        _empleado = empleado.objects.get(usuario=self.request.user)
        if _empleado.empresa=="2" and _empleado.id_empleado_especialidad==2:
            return HttpResponseRedirect(reverse(dashboardRecepcionView,args=[self.request.user]))
        return reverse_lazy("asilo:home")
    
    
    
class logout(LoginView):
    def get(self, request, *args, **kwargs):
        logout(request)