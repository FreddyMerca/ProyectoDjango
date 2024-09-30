from django.http import HttpResponse
import datetime

def saludo(request):

    return HttpResponse ("Mensaje de Saludo para la primera vista del uso del Django")

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

def calculaEdad(request, agno):

    edadActual=37
    periodo=agno-2024
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el Año %s tendras %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)

