

from django.db.models import Q
from collections import OrderedDict
from itertools import chain
from asilo.models import expediente
from contabilidad.models import cobro
from fundacion.models import factura


class reporteMixin:
    
    def __init__(self) -> None:
        pass
    
    
    def get_cobro(self):
        cobros = cobro.objects.all()
        facturas = []
        for _cobro in cobros:
            if _cobro.id_factura not in facturas:
                facturas.append(_cobro.id_factura)
        return facturas
    
    def get_cobro_by_usuario(self, cliente, value):
        
        facturas = []
        cobros = cobro()
        if cliente == 1: # DPI
            print(f"buscar por DPI")
            cobros = cobro.objects.filter(id_factura__id_ficha__id_expediente__id_datosPersonales__dni=value)
        if cliente == 2: # expediente
            print("buscar por expediente")
            facturas = factura.objects.filter(id_ficha__id_expediente=2)
            print(facturas)
            cobros = cobro.objects.filter(id_factura__in=facturas)
        for _cobro in cobros:
            if _cobro.id_factura not in facturas:
                facturas.append(_cobro.id_factura)
        print(f"------> {cobros}")
        return facturas
    
    def get_cobro_by_date(self, fechaInit, fechaFin):
        cobros = cobro.objects.all()
        facturas = []
        for _cobro in cobros:
            if _cobro.id_factura not in facturas:
                facturas.append(_cobro.id_factura)
        return facturas
    
    
    