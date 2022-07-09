from fundacion.models import facturaDetalleFarmacia, facturaDetalleEspecialidad
from contabilidad.models import cobro

class contabilidadMixin:


    def get_total(item=None, factura=None):
        total = 0
        farmacia = facturaDetalleFarmacia.objects.filter(id_factura=factura.id_factura).values("precio_unitario","cantidad")
        especialidades = facturaDetalleEspecialidad.objects.filter(id_factura=factura.id_factura).values("costo")
        cobros  = cobro.objects.filter(id_factura = factura.id_factura)
        for item in farmacia:
            total += item['precio_unitario']*item['cantidad'] 
        for item in especialidades:
            total += item['costo']

        for item in cobros:
            total = total-item.id_transaccion.monto
        return total