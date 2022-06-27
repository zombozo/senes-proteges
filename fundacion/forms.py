from django import forms
from .models import consultaMedica,  solicitudCita, solicitudCitaDetalle, tratamiento


class consultaMedicaForm( forms.ModelForm):
    class Meta:
        model = consultaMedica
        fields = ["diagnostico"]
        
        
        
class tratamientoForm( forms.ModelForm):
    class Meta:
        model = tratamiento
        fields = ["medicamento", "id_enfermedad", "descripcion"]
    def __init__(self, *args, **kwargs):
        super(tratamientoForm, self).__init__(*args, **kwargs)
        

class solicitudCitaForm(forms.ModelForm):
    pagina = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput())
    class Meta:
        model = solicitudCita
        fields = ["id_enfermero","descripcion"]
        

    def __init__(self, *args, **kwargs):
        super(solicitudCitaForm, self).__init__(*args, **kwargs)
        self.fields["pagina"].initial = "solicitud"




class solicitudCitaDetalleForm(forms.ModelForm):
    pagina = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    class Meta:
        model = solicitudCitaDetalle
        fields = ["id_especialidad", "descripcion"]


    def __init__(self, *args, **kwargs):
        super(solicitudCitaDetalleForm, self).__init__(*args, **kwargs)
        self.fields["pagina"].initial ="detalle"


class solicitudCitaDetalleFechaForm(forms.ModelForm):
    class Meta:
        model = solicitudCitaDetalle
        fields = ["fecha_hora"]


    def __init__(self, *args, **kwargs):
        super(solicitudCitaDetalleFechaForm, self).__init__(*args, **kwargs)
