from django.urls import path

from libro.views import InicioListView, DetalleLibroView, CrearLibroView

urlpatterns = [
    path('', InicioListView.as_view(), name='listar'),
    path('libro/<int:libro_id>/detalles/', DetalleLibroView.as_view(), name='detalles'),
    path('libro/añadir', CrearLibroView.as_view(), name='crear'),
]