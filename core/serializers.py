from rest_framework import serializers
from .models import Pelicula


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'duracion', 'anio', 'genero', 'sinopsis', 'fecha_estreno']