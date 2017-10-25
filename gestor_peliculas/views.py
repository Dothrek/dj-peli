from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from .models import Pelicula, Actor

def pelis(request):
    datos = serializers.serialize("json", Pelicula.objects.all())
    #   array_datos = json.loads(datos)
    # new_array_datos = []
    # for elem in array_datos:
    #     new_array_datos.append(elem["fields"])

    new_array_datos = list(map(lambda x : x["fields"], json.loads(datos)))

    return JsonResponse(new_array_datos, safe=False)

def p2(request):
    data = serializers.serialize("json", Pelicula.objects.all())
    return HttpResponse(data, content_type='application/json')
