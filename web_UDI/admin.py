from django.contrib import admin

# Register your models here.
from .models import Usuario, Mensaje

# Registrar el modelo Usuario en el panel de administración
admin.site.register(Usuario)
admin.site.register(Mensaje)