from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name='home'),
    path('galeria/',galeria, name='galeria'),
    path('listado_peliculas/',listado_pelicula, name='listado_peliculas'),
    path('nueva_pelicula/',nueva_pelicula, name='nueva_pelicula'),
    path('modificar_pelicula/<id>/', modificar_pelicula, name="modificar_pelicula"),
    path('eliminar_pelicula/<id>/', eliminar_pelicula, name="eliminar_pelicula"),

]