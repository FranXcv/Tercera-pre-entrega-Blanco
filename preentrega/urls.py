from django.urls import path, include
from preentrega.views import *

urlpatterns = [
    path('', index, name="index"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profe"),
    path("cursos/", cursos, name="cursos"),
    path("entregables/", entregables, name="entregables"),
]