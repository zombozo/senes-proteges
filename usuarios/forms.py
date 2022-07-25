
from django import forms
from usuarios.models import datosPersonales
from django.forms import ModelForm, DateInput


class datosPersonalesForm(ModelForm):
    
    class Meta:
        model = datosPersonales
        fields = "__all__"
        widgets = {
            'fecha_nacimiento': DateInput(
                        format=('%d %B, %Y'),
                        attrs={
                            "class":"datepicker",
                        })
        }
        # "type":"date"
    def __init__(self, *args, **kwargs):
        super(datosPersonalesForm, self).__init__(*args, **kwargs)
        print("init form")
        self.fields["fecha_nacimiento"].widget = forms.widgets.DateInput(
                    attrs={
                        "class":"form-control",
                        "type":"date"
                    }
                )
                
