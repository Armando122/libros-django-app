from django import forms

from libro.models import Libro

"""
Clase para crear una instancia de la clase de libro.
"""
class LibroCrearForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'sinopsis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sinopsis'}),
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date' , 'class': 'form-control', 'placeholder': 'Fecha Publicacion'}),
            'portada': forms.FileInput(attrs={'type': 'file', 'class': 'form-control-file', 'placeholder': 'Portada'}),
        }