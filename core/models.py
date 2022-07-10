from audioop import maxpp
from django.db import models


class Genero(models.Model):
    nombre= models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre=models.CharField(max_length=200)
    duracion= models.IntegerField()
    anio=models.IntegerField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre