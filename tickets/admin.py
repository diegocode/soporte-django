from django.contrib import admin
from .models import Ticket

class TicketAdm(admin.ModelAdmin):
    list_display = ('tipo', 'fecha_reporte', 'nombre', 'telefono', 'estado')
    list_filter  = ('tipo', 'estado')
    search_fields = ('nombre', 'telefono', 'descripcion')


admin.site.register(Ticket, TicketAdm)
