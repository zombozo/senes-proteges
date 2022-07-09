from django import forms
from django.db import models
from .models import donacion, transaccion,pago

class donacionForm(forms.ModelForm):
    monto = forms.IntegerField()
    class Meta:
        model = donacion
        fields = ["monto","nombre", "id_donante" ]


class pagosForm(forms.ModelForm):
    monto = forms.IntegerField()
    class Meta:
        model = pago
        fields = ["id_servicio", "monto"]

