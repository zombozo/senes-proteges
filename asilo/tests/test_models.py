import datetime
from django.test import TestCase
from datetime import date
from asilo.models import expediente
from django.template.defaultfilters import slugify

from usuarios.models import datosPersonales

# Create your tests here.


class ExpedienteModelTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_expediente_tiene_codigoExp(self):
        fechaNac = date.fromisoformat('1999-12-21')
        _datosPersonales = datosPersonales.objects.create(fecha_nacimiento=fechaNac)
        expedientes = expediente.objects.create(id_datosPersonales=_datosPersonales)
        expedientes.save()
        self.assertEqual(f"sp-{expedientes.id_expediente}", slugify(f"SP-{expedientes.id_expediente}"))
        


