from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cursos(request):
    return render(request, "preentrega/cursos.html")

def profesores(request):
    return render(request, "preentrega/profesores.html")

def estudiantes(request):
    return render(request, "preentrega/estudiantes.html")

def entregables(request):
    return render(request, "preentrega/entregables.html")

def index(request):
    return render(request, "preentrega/index.html")
