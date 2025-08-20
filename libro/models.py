from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    sinopsis = models.TextField()
    portada = models.ImageField(null=True, blank=True, upload_to="recursos/portadas/")
    # precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return f'{self.titulo} | {self.isbn}'