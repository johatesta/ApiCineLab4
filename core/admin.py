from django.contrib import admin
from .models import *

class PeliculaAdimin(admin.ModelAdmin):
    list_display= ['nombre','duracion','anio','genero']
    search_fields= ['nombre','anio']
    list_filter= ['genero']
    list_per_page = 10

admin.site.register(Genero)

admin.site.register(Pelicula)