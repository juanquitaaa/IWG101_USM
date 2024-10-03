from django.urls import path
from . import views  # Asegúrate de que esto esté importando correctamente

urlpatterns = [
    path('', views.index, name='index'),  # Define la URL para la vista index
]
