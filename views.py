from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre
        self.apellido=apellido

        
def saludo(request):

    p1=Persona("Profesor Jair", "Jirafales")
    
    #nombre="Freddy"
    #apellido="Mercado"

    temas2=[]
    temas3=[]
    ahora=datetime.datetime.now()
    doc_externo=open("D:/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas2}) #Asiganacion de una clave a un valor alamacenado ne una variable
    
    documento=plt.render(ctx)

    return HttpResponse (documento)

def despedida(request):

    return HttpResponse("Segundo mensaje de Django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>
    """ %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):

    #edadActual=37
    periodo=agno-2024
    edadFutura=edad+periodo
    documento="<html><body><h2>En el Año %s tendras %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)

