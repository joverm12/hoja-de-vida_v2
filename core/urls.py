from django.contrib import admin
from django.urls import path
from cv.views import home

# SEGURIDAD: Esto quita la marca "Django" del panel de administración
admin.site.site_header = "SISTEMA DE GESTIÓN PROFESIONAL" 
admin.site.site_title = "Panel Administrativo"
admin.site.index_title = "Bienvenido al Gestor de Contenido"

urlpatterns = [
    path('admin/', admin.site.urls), # El Admin sigue protegido por su cuenta
    path('', home, name='home'),     # Tu CV es PÚBLICO (Cualquiera lo ve siempre)
]