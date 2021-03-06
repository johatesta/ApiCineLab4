from django.db import router
from django.urls import include, path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('peliculas', PeliculaViewSet)


urlpatterns = [
    path('', home,name='home'),
    path('galeria/',galeria, name='galeria'),
    path('listado_peliculas/',listado_pelicula, name='listado_peliculas'),
    path('nueva_pelicula/',nueva_pelicula, name='nueva_pelicula'),
    path('modificar_pelicula/<id>/', modificar_pelicula, name="modificar_pelicula"),
    path('eliminar_pelicula/<id>/', eliminar_pelicula, name="eliminar_pelicula"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('api/', include(router.urls)),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)