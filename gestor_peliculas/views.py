from django.http import JsonResponse

from .models import Pelicula, Actor

def pelis(request):
    peliculas = Pelicula.objects.prefetch_related('actores')

    try:
        pelis = list(map(lambda x : x.to_api_obj(), peliculas))
        error = False
    except Exception as e:
        pelis = []
        error = True
    return JsonResponse({"data":pelis, "err":error}, safe=False)

def actores(request):
    actores = Actor.objects.all()

    try:
        json_actores = list(map(lambda x : x.to_api_obj(), actores))
        error = False
    except Exception as e:
        json_actores = []
        error = True
    return JsonResponse({"data":json_actores, "err":error}, safe=False)

def actorId(request, actor_id):
    actor = Actor.objects.all().filter(id = actor_id).all()
    print(actor)

    try:
        json_actor = list(map(lambda x : x.to_api_obj(), actor))
        error = False
    except Exception as e:
        json_actor = []
        error =True
    return JsonResponse({"data":json_actor, "err":error}, safe=False)
