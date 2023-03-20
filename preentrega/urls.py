from django.urls import path, include
from preentrega.views import inicio, cursos, profesores, estudiantes, entregables, index

urlpatterns = [
    path('', inicio),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("cursos/", cursos),
    path("entregables/", entregables),
    path("index/", index),
]