from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pelis$', views.pelis, name='pelis'),
]
