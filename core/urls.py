from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name='home'),
    path('galeria/',galeria, name='galeria'),
    path('listado_peliculas/',listado_pelicula, name='listado_peliculas'),
     path('nueva_pelicula/',nueva_pelicula, name='nueva_pelicula')

]