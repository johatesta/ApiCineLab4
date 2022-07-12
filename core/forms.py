from django import forms
from django.forms import ModelForm
from .models import Pelicula
import datetime

class PeliculaForm(ModelForm):
    nombre = forms.CharField(min_length=2,max_length=200)
    duracion = forms.IntegerField(min_value=5, max_value=500)
    class Meta:
        model=Pelicula
        fields=['nombre','duracion','anio','genero','fecha_estreno','sinopsis','imagen']

def clean_fecha_estreno(self):
    fecha = self.cleaned_data['fecha_estreno']
    if fecha > datetime.date.today():
        raise forms.ValidationError("Fecha no puede ser mayor al dia de hoy")
    
    return fecha