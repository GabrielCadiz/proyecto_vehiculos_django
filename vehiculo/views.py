from .models import Vehiculo
from django.shortcuts import render, redirect
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Permission



def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            form = VehiculoForm()
            return redirect(request, 'vehiculo/agregar_vehiculo.html')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = "Bajo"
        elif vehiculo.precio <= 30000:
            vehiculo.condicion_precio = "Medio"
        else:
            vehiculo.condicion_precio = "Alto"
    return render(request, 'vehiculo/list.html', {'vehiculos': vehiculos})

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_vehiculo')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

def index(request):
    return render(request, 'vehiculo/index.html')
    

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente tras el registro
            # Asignar el permiso 'visualizar_catalogo' al nuevo usuario
            permiso = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permiso)
             # Asignar el permiso 'add_vehiculo' al nuevo usuario
            permiso = Permission.objects.get(codename='add_vehiculo')
            user.user_permissions.add(permiso)
            return redirect('index')  # Redirige al inicio o a cualquier otra página
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})







