
from usuarios.models import datosPersonales
from django.forms import ModelForm, DateInput


class datosPersonalesForm(ModelForm):
    
    class Meta:
        model = datosPersonales
        fields = "__all__"
        widgets = {
            'fecha_nacimiento': DateInput(attrs={'class':'form-control', 'type':'date'}),
        }
        
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields['fecha_nacimiento'].widget.attrs.update({'type':'date'})
