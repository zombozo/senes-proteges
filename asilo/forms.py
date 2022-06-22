

from email.policy import default
from django import forms
from asilo.models import contacto
from fundacion.models import solicitudCita, solicitudCitaDetalle


class contactoForm(forms.ModelForm):
    
    class Meta:
        model = contacto
        fields = "__all__"
        