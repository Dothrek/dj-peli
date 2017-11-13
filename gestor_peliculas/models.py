from django.db import models

# Create your models here.

class Actor(models.Model):
    nombre = models.CharField(max_length=50,)
    fecha_nac = models.IntegerField()
    foto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def to_api_reference(self):
        return  {"id": self.pk, "nombre": self.nombre}

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    actores = models.ManyToManyField(Actor)

    def __str__(self):
        return self.titulo

    def to_api_obj(self):
        return {
            "titulo": self.titulo,
            "imagen": self.imagen,
            "descripcion": self.descripcion,
            "actores": list(map(lambda x : x.to_api_reference(), self.actores.all()))
        }

    def to_api_reference(self):
        return  {"id": self.pk, "titulo": self.titulo}
