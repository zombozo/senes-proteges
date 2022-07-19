from django import forms

from usuarios.models import empleado
from .models import clienteEnfermedad, consultaMedica, enfermedad,  solicitudCita, solicitudCitaDetalle, solicitudLaboratorio, tratamiento


class consultaMedicaForm( forms.ModelForm):
    class Meta:
        model = consultaMedica
        fields = ["diagnostico"]
        
        
class tratamientoForm( forms.ModelForm):
    class Meta:
        model = tratamiento
        fields = ["medicamento","cantidad", "descripcion"]
    def __init__(self, *args, **kwargs):
        super(tratamientoForm, self).__init__(*args, **kwargs)
        

class solicitudCitaForm(forms.ModelForm):
    pagina = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput())
    class Meta:
        model = solicitudCita
        fields = ["id_enfermero","descripcion"]
        

    def __init__(self, *args, **kwargs):
        super(solicitudCitaForm, self).__init__(*args, **kwargs)
        choices = [(empleado.id_empleado, empleado.id_datos_personales.get_nombreCompleto()) for empleado in  empleado.objects.filter(id_empleado_especialidad__nombre__icontains="Enfermeria")]
        self.fields["id_enfermero"].choices = choices
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


class solicitudLaboratorioForm(forms.ModelForm):
    class Meta: 
        model = solicitudLaboratorio
        fields = ["id_tipoLaboratorio","descripcion"]
        

class enfermedadForm(forms.ModelForm):
    class Meta:
        model = clienteEnfermedad
        fields = ["id_enfermedad", "descripcion", "estado"]