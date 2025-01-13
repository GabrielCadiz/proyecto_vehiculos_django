# Proyecto Vehículos Django

Este es un proyecto de gestión de vehículos desarrollado con Django. Permite agregar, listar y administrar vehículos, mostrando información como la marca, modelo, serial, precio, etc.

## Requisitos

- Python 3.x
- Django 4.x
- Base de datos (SQLite por defecto)

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

1. **Clona el repositorio en tu máquina local:**
   ```bash
   git clone https://github.com/GabrielCadiz/proyecto_vehiculos_django.git

Instala las dependencias: Crea un entorno virtual y activa el entorno, luego instala las dependencias necesarias.

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

Configura la base de datos: Ejecuta las migraciones para crear las tablas necesarias:

python manage.py migrate

Ejecuta el servidor de desarrollo:

python manage.py runserver

Accede a la aplicación: Abre un navegador y accede a http://localhost:8000/

Uso
Puedes agregar vehículos a través del formulario de la interfaz de administración.
Los vehículos agregados se pueden listar y visualizar en el sistema.
Contribuciones
Si deseas contribuir a este proyecto, haz un fork del repositorio, crea una rama con tus cambios y envía un pull request.