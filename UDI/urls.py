"""
URL configuration for UDI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from web_UDI import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index, name='index'),
    path("register/",views.register, name='register'),
    path('test/',views.test, name='test'),
    path('error/',views.error, name='error'),
    path('posting/', views.posting, name='posting'),
    path('delete/<int:mensaje_id>/', views.delete, name='delete'),
    path('avisos/', views.crear_aviso, name='avisos'),
    path('ajustes/', views.settings, name='ajustes'),
    path('settings/', views.settings, name='settings'),
    path('actualizar/<int:usuario_id>/', views.actualizar_perfil, name='actualizar_perfil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)