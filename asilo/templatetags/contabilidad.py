from django import template
from contabilidad.mixins import contabilidadMixin


register = template.Library()

@register.filter(name='total')
def total(factura, args):
    return contabilidadMixin.get_total(factura=factura)