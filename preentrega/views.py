from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "preentrega/inicio.html")

def cursos(request):
    return HttpResponse("vista cursos")

def profesores(request):
    return HttpResponse("vista profesores")

def estudiantes(request):
    return HttpResponse("vista estudiantes")

def entregables(request):
    return HttpResponse("vista entregbales")

def index(request):
    return render(request, "preentrega/index.html")
