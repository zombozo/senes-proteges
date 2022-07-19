from fundacion.models import facturaDetalleFarmacia, facturaDetalleEspecialidad, facturaDetalleLaboratorio
from contabilidad.models import cobro

class contabilidadMixin:


    def get_total(item=None, factura=None):
        total = 0
        farmacia = facturaDetalleFarmacia.objects.filter(id_factura=factura.id_factura).values("precio_unitario","cantidad","descuento")
        especialidades = facturaDetalleEspecialidad.objects.filter(id_factura=factura.id_factura).values("costo","descuento")
        laboratorios = facturaDetalleLaboratorio.objects.filter(id_factura = factura.id_factura).values("costo", "descuento")
        cobros  = cobro.objects.filter(id_factura = factura.id_factura)
        for item in farmacia:
            descuentoPorcentaje = int(item['descuento'] or 0)
            porcentaje = descuentoPorcentaje/100
            sub_total = item['precio_unitario']*item['cantidad']
            descuento = sub_total*porcentaje
            print(f"descuento de farmacia -> {descuentoPorcentaje}:{descuento} sin descuento: {sub_total} with descuento: {sub_total - descuento}")
            total += sub_total - descuento
        for item in especialidades:
            descuentoPorcentaje = int(item['descuento'] or 0)
            porcentaje = descuentoPorcentaje/100
            sub_total = item['costo']
            descuento = sub_total*porcentaje
            print(f"descuento de especialidades -> {descuentoPorcentaje}:{descuento} sin descuento: {sub_total} with descuento: {sub_total - descuento}")
            total += sub_total - descuento
        for item in laboratorios:
            descuentoPorcentaje = int(item['descuento'] or 0)
            porcentaje = descuentoPorcentaje/100
            sub_total = item['costo']
            descuento = sub_total*porcentaje
            print(f"descuento de laboratorios -> {descuentoPorcentaje}:{descuento} sin descuento: {sub_total} with descuento: {sub_total - descuento}")
            total += sub_total - descuento
            
        for item in cobros:
            total = total-item.id_transaccion.monto
        return total
    
    
    
    def get_totalFactura(item=None, factura=None):
        total = 0
        farmacia = facturaDetalleFarmacia.objects.filter(id_factura=factura.id_factura).values("precio_unitario","cantidad","descuento")
        especialidades = facturaDetalleEspecialidad.objects.filter(id_factura=factura.id_factura).values("costo","descuento")
        laboratorios = facturaDetalleLaboratorio.objects.filter(id_factura = factura.id_factura).values("costo", "descuento")
        cobros  = cobro.objects.filter(id_factura = factura.id_factura)
        for item in farmacia:
            sub_total = item['precio_unitario']*item['cantidad']
            total += sub_total
        for item in especialidades:
            sub_total = item['costo']
            total += sub_total

        for item in laboratorios:
            sub_total = item['costo']
            total += sub_total
        return total
    
    
    
