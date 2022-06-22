from curses.ascii import NUL
from django.views.generic import ListView
from django.shortcuts import render

from asilo.models import expediente

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