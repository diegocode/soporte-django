from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Ticket

# vista para probar
# copiada de la documentación de django:
# https://docs.djangoproject.com/en/4.0/topics/http/views/
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def listar_tickets(request):
    datos = Ticket.objects.all()
    return render(request, 'tickets/lista_tickets.html', {'lista_tickets': datos})
