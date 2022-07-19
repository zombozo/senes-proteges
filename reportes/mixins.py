

from django.db.models import Q
from collections import OrderedDict
from itertools import chain
from asilo.models import expediente
from contabilidad.models import cobro, donacion, pago
from fundacion.models import consultaMedica, factura, tratamiento


class reporteMixin:
    
    def __init__(self) -> None:
        pass
    
    def get_factura_by_usuario(self, cliente,  opcion):
        facturas = []
        if int(opcion)== 1: #DPI
            facturas = factura.objects.filter(id_ficha__id_expediente__id_datosPersonales__dni=cliente)
        elif int(opcion) == 2:
            facturas = factura.objects.filter(id_ficha__id_expediente=opcion)
        return facturas
    
    
    def get_factura_by_date(self, dateInit, dateFin):
        facturas = []
        facturas = factura.objects.filter(fecha__range=[dateInit, dateFin])
        return facturas
    
    def get_consultas_by_cliente(self, cliente, opcion):
        consultas = []
        if int(opcion) == 1: #dpi
            consultas = consultaMedica.objects.filter(id_ficha__id_expediente__id_datosPersonales__dni=cliente)
        elif int(opcion) == 2: #expediente
            consultas = consultaMedica.objects.filter(id_ficha__id_expediente=opcion)
        return consultas
    
    def get_consultas_by_date(self, dateInit, dateFin):
        return consultaMedica.objects.filter(creado_en__range=[dateInit, dateFin])
    
    
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
            print(cobros)
        if cliente == 2: # expediente
            facturas = factura.objects.filter(id_ficha__id_expediente=value)
            cobros = cobro.objects.filter(id_factura__in=facturas)
        for _cobro in cobros:
            if _cobro.id_factura not in facturas:
                facturas.append(_cobro.id_factura)
        return facturas
    
    def get_cobro_by_date(self, fechaInit, fechaFin):
        cobros = cobro.objects.filter(id_transaccion__fecha__range=[fechaInit, fechaFin])
        facturas = []
        for _cobro in cobros:
            if _cobro.id_factura not in facturas:
                facturas.append(_cobro.id_factura)
        return facturas
    
    
    def get_pagos_by_date(self, fechaInit, fechaFin):
        pagos = pago.objects.filter(id_transaccion__fecha__range=[fechaInit, fechaFin])
        return pagos
    
    
    def get_pagos_by_nombre_servicio(self, nombre):
        pagos = pago.objects.filter(id_servicio__nombre=nombre)
        return pagos
    
    def get_donaciones_by_fecha(self, fechaInit, fechaFin):
        donaciones = donacion.objects.filter(id_transaccion__fecha__range=[fechaInit, fechaFin])
        return donaciones
    
    
    def get_donaciones_by_donante(self, donante):
        donaciones = donacion.objects.filter(nombre__icontains=donante)
        return donaciones
    
    
    def get_medicamentos_by_cliente(self, cliente, opcion):
        tratamientos = []
        if int(opcion) == 1:
            tratamientos = tratamiento.objects.filter(id_ficha__id_expediente__id_datosPersonales__dni=cliente)
            
        elif int(opcion) == 2:
            tratamientos = tratamiento.objects.filter(id_ficha__id_expediente=cliente)
        
        return tratamientos
    
    
    def get_medicamentos_by_date(self, fechaInit, fechaFin):
        tratamientos = []
        tratamientos = tratamiento.objects.filter(fecha__range=[fechaInit, fechaFin])
        
        return tratamientos
    
    