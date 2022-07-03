from audioop import reverse
from curses.ascii import NUL
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.views import LoginView

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
            _search = int(search)
            print(f"-- {_search}")
            expedientes = expediente.objects.filter(id_datosPersonales__dni=_search)
            print(expedientes)
        if opcion == "2":
            expedientes = expediente.objects.filter(id_datosPersonales__primer_nombre__startswith=search )
        if opcion == "3":
            expedientes = expediente.objects.filter(id_datosPersonales__primer_apellido__startswith=search)
        if opcion == "4":
            expedientes = expediente.objects.filter(codigo_expediente__startswith=search)
        context = {
            "expedientes": expedientes
        }
        print(context)
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