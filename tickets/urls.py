from django.urls import path, include
from . import views

urlpatterns = [
    path('ahora/', views.current_datetime, name='test_urls')
]
