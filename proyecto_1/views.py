from django.http import HttpResponse

from datetime import date, datetime

def saludo(request, nombre):
    return HttpResponse(f"hola que tal {nombre}")
def despedida(request):
    return HttpResponse("chau hasta luego")
def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = (f"hoy es {fecha}")
    return HttpResponse(mensaje)