from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def DiaDeHoy(request):

    hoy = dt.now()
    return HttpResponse(f"El dia y hora de hoy es:\n<br>{hoy}")

def Minombre(self, nombre):
    DocumentodeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse(DocumentodeTexto)

def Probandotemplate(self):
    #miHtml = open("./templates/template1.html")
    #plantilla = Template(miHtml.read())
    #miHtml.close()

    plantilla = loader.get_template("template1.html")
    notas = [10,9,4,9,15,1]
    mis_datos = {"nombre": "Franco", "apellido": "Blanco", "notas": notas}
    
    #mi_contexto = Context(mis_datos)

    #documento = plantilla.render(mis_datos)
    documento = plantilla.render(mis_datos)

    return HttpResponse(documento)