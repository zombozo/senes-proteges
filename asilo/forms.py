from django import forms
from asilo.models import contacto
from fundacion.models import solicitudCita, solicitudCitaDetalle


class contactoForm(forms.ModelForm):
    
    class Meta:
        model = contacto
        excludes = ["id_expediente"]
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_nacimiento"].widget = forms.widgets.DateTimeInput()