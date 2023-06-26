from django.urls import path
from .views import Inicio, ConsolaPage, CelularPage, ComputadoraPage, AgregarPublicacion, ConsolaDetalle, ComputadoraDetalle, CelularDetalle, ComentarioPage, LoginPage, Registro

urlpatterns = [
    path('inicio/', Inicio.as_view(), name='Inicio'),
    path('listaConsola/', ConsolaPage.as_view(), name='Consola'),
    path('listaCelular/', CelularPage.as_view(), name='Celular'),
    path('listaComputadora/', ComputadoraPage.as_view(), name='Computadora'),
    path('detalleConsola/<int:pk>/', ConsolaDetalle.as_view(), name='consola'),
    path('detalleCelular/<int:pk>/', CelularDetalle.as_view(), name='celular'),
    path('detalleComputadora/<int:pk>/', ComputadoraDetalle.as_view(), name='computadora'),
    path('detalleConsola/<int:pk>/comentario/', ComentarioPage.as_view(), name='comentario'),
    path('detalleCelular/<int:pk>/comentario/', ComentarioPage.as_view(), name='comentario'),
    path('detalleComputadora/<int:pk>/comentario/', ComentarioPage.as_view(), name='comentario'),
    path('agregarPublicacion/', AgregarPublicacion.as_view(), name='AgregarPublicacion'),
    path('login/', LoginPage.as_view(), name='Login'),
    path('registro/', Registro.as_view(), name='Registro')
]


