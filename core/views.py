from django.shortcuts import redirect, render
from .models import *
from .forms import Pelicula
from .forms import PeliculaForm

def home(request):
    data = {
        'peliculas':Pelicula.objects.all()
    }
    return render(request,'core/index.html', data)



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

    if request.method == 'POST':
        formulario=PeliculaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Datos Guardados Correctamente"
        data['form'] = formulario
    return render(request,'core/nueva_pelicula.html', data)


def modificar_pelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    data = {
        'form': PeliculaForm(instance = pelicula)
    }
    if request.method == 'POST':
        formulario = PeliculaForm(data = request.POST, instance = pelicula, files = request.FILES) 
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Pelicula modificado con éxito'
        data['form'] = PeliculaForm(instance = Pelicula.objects.get(id = id)) 

    return render(request,'core/modificar_pelicula.html',data)


def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()

    return redirect(to="listado_peliculas")