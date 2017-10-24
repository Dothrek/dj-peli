from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Pelicula, Actor

def pelis(request):
    lista_pelis = Pelicula.objects.all()
    datos = serializers.serialize("json", lista_pelis)
    return render(request, 'gestorPeliculas/peliculas.html', {'datos': datos})
