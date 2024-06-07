from django import forms

class CrearUserFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()