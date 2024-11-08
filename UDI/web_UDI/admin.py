from django.contrib import admin

# Register your models here.
from .models import Usuario

# Registrar el modelo Usuario en el panel de administración
admin.site.register(Usuario)