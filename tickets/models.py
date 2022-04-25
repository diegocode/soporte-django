from django.db import models
from django.utils import timezone

class Ticket(models.Model):
   ESTADOS = (               # estados para 'estado'
       ('P', 'Pendiente'),   # el primer elemento es lo que se guarda
       ('C', 'Cerrado'),     # el segundo lo que se muestra
       ('E', 'En curso'),    # ej. se muestra Cerrado, se guarda C
   )

   TIPOS = (
        ('H', 'Hardware'),
        ('S', 'Software'),
        ('C', 'Conectividad'),
        ('I', 'Insumos'),
        ('X', 'Otro'),
   )

   tipo = models.CharField(max_length=1,
                            choices=TIPOS,
                            default='X')

   nombre = models.CharField(max_length=60)
   email = models.EmailField(max_length=120)
   telefono=models.CharField(max_length=60)

   estado = models.CharField(max_length=1,
                            choices=ESTADOS,
                            default='P')

   descripcion = models.CharField(max_length=250, default="")

   fecha_reporte = models.DateTimeField(default=timezone.now)
   fecha_resuelto = models.DateTimeField(blank=True, null=True)

   class Meta:
       # ordenado por fecha de reporte, desc
       ordering = ('-fecha_reporte',)

   def __str__(self):
       # fecha_reporte - nombre usuario
       return str(self.fecha_reporte.isoformat(timespec='minutes')) + '-' + str(self.nombre)

