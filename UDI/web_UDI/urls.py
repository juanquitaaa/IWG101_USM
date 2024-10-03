from django.urls import path, include
from django.contrib import admin
from . import views  # Asegúrate de que esto esté importando correctamente

urlpatterns = [
    path('', views.index, name='index'),
]
 