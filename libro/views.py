from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination

from libro.forms import LibroCrearForm
from libro.models import Libro
from libro.serializers import LibroSerializer


# Create your views here.
class InicioListView(GenericAPIView):
    serializer_class = LibroSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20

    def get_queryset(self):
        return Libro.objects.all()

    def get(self, request):
        libros = self.get_queryset()
        serializer = LibroSerializer(libros, many=True)
        return render(request, 'inicio.html', {'libros': serializer.data})

class DetalleLibroView(GenericAPIView):
    serializer_class = LibroSerializer

    def get(self, request, libro_id):
        libro = Libro.objects.get(id=libro_id)
        serializer = LibroSerializer(libro)
        return render(request, 'detalle.html', {'libro': serializer.data})

"""
Clase para añadir nuevos libros
"""
class CrearLibroView(CreateAPIView, GenericAPIView):
    serializer_class = LibroSerializer

    def get(self, request):
        formulario = LibroCrearForm()
        return render(request, 'crear-libro.html', {'form': formulario})

    def post(self, request, *args, **kwargs):
        formulario = LibroCrearForm(request.POST, request.FILES)

        if formulario.is_valid():
            # nuevo_libro = formulario.save(commit=False)
            # nuevo_libro.save())
            formulario.save()
            return redirect('listar')
        return redirect('crear')

