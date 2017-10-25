from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from .models import Pelicula, Actor

def pelis(request):
    datos = serializers.serialize("json", Pelicula.objects.all())
    json_datos = json.dumps(datos)
    return JsonResponse(datos, safe=False)
