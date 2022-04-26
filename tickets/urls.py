from django.urls import path, include
from . import views

urlpatterns = [
    path('ahora/', views.current_datetime, name='tickets_ahora'),
    path('lista/', views.listar_tickets, name='tickets_lista'),
]
