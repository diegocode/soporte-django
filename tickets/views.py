from django.http import HttpResponse
import datetime

# vista para probar
# copiada de la documentación de django:
# https://docs.djangoproject.com/en/4.0/topics/http/views/
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

