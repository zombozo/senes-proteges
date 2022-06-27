from django import template


register = template.Library()

@register.filter(name='especialidad')
def especialidad(id_usuario, args):
    print(id_usuario)
    print("Especialidad del empleado")
    return "recepcionista"