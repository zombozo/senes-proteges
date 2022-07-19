from django import template

from usuarios.models import empleado


register = template.Library()

@register.filter(name='especialidad')
def especialidad(id_usuario, args):
    _empleado = empleado.objects.get(usuario=id_usuario)
    return _empleado.id_datos_personales.get_nombreCompleto()