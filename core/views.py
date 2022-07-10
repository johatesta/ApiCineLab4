from django.shortcuts import render
from .models import *
from .forms import PeliculaForm

def home(request):
    return render(request,'core/index.html')



def galeria(request):
     return render(request,'core/galeria.html')


def listado_pelicula(request):
    peliculas=Pelicula.objects.all()
    data={
        'peliculas':peliculas
    }
    return render(request, 'core/listado_peliculas.html',data)
    

def nueva_pelicula(request):
    data={
        'form':PeliculaForm()
    }

    if request.method== 'POST':
        formulario=PeliculaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Datos Guardados Correctamente"
    return render(request,'core/nueva_pelicula.html',data)