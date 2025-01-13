# vehiculo/urls.py
from django.urls import path
from . import views
from .views import agregar_vehiculo

urlpatterns = [
    path('add', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('list', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculo/add', agregar_vehiculo, name='agregar_vehiculo'),
]
