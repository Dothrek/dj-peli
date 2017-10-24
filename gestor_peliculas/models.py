from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    actores = models.ManyToManyField('Actor')
    def __str__(self):
        return self.titulo

class Actor(models.Model):
    nombre = models.CharField(max_length=50,)
    fecha_nac = models.IntegerField()
    foto = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
