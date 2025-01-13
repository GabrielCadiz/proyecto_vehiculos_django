from django.apps import AppConfig

class VehiculoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehiculo'

    def ready(self):
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType
        from .models import Vehiculo

        content_type = ContentType.objects.get_for_model(Vehiculo)
        Permission.objects.get_or_create(codename='visualizar_catalogo', name='Puede visualizar catálogo', content_type=content_type)

