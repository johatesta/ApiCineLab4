from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Pelicula

class PeliculaForm(ModelForm):
    class Meta:
        model=Pelicula
        fields=['nombre','duracion','anio','genero','fecha_estreno','sinopsis','imagen']