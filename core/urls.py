from django.contrib import admin
from django.urls import path, include # Asegúrate de agregar 'include' aquí
from cv.views import home

# ESTO CUMPLE LO QUE PIDIÓ TU PROFESOR:
# Solo cambia el Admin, el CV sigue igual.
admin.site.site_header = "SISTEMA DE GESTIÓN" 
admin.site.site_title = "Portal Administrativo"
admin.site.index_title = "Bienvenido"

urlpatterns = [
    path('admin/', admin.site.urls), # El admin sigue en su ruta
    # AGREGA ESTA LÍNEA para que el error NoReverseMatch desaparezca:
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', home, name='home'),
]