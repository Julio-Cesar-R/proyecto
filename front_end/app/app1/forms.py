
from tkinter import Widget
from django import forms
from .models import Demostracion

class DemostracionForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Demostracion
        fields = (
            'dato1',
            'dato2',
            'dato3',
            
            )

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)    
    apellido_paterno = forms.CharField( max_length=50, required=False)
    apellido_materno = forms.CharField( max_length=50, required=False)
    edad=forms.IntegerField()
    email = forms.EmailField( required=False)
    telefono = forms.CharField( max_length=10, required=False)
