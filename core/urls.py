from django.contrib import admin
from django.urls import path
from cv.views import home

# PROTECCIÓN DE FOOTPRINTING: Cambia los nombres para que no diga Django
admin.site.site_header = "SISTEMA DE GESTIÓN PROFESIONAL" 
admin.site.site_title = "Panel Administrativo" 
admin.site.index_title = "Bienvenido al Gestor de Contenido"

urlpatterns = [
    path('admin/', admin.site.urls), # El admin sigue protegido por su propio login
    path('', home, name='home'),     # Tu CV sigue público para todo el mundo
]