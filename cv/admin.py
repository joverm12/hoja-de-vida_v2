from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db import models  # Necesario para detectar los campos de fecha
from django import forms     # Necesario para el widget del calendario
from .models import *

# 1. LIMPIEZA DEL PANEL (Solo tus modelos de la ULEAM)
admin.site.unregister(User)
admin.site.unregister(Group)

# 2. CONFIGURACIÓN MAESTRA PARA TODAS LAS SECCIONES
class MiHojaDeVidaAdmin(admin.ModelAdmin):
    exclude = ('perfil',) # Oculta el campo perfil siempre
    
    # ESTO ACTIVA EL SELECTOR DE FECHA COMPLETO (DÍA/MES/AÑO) EN TODAS LAS SECCIONES
    formfield_overrides = {
        models.DateField: {
            'widget': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'vDateField',
                    'style': 'width: 200px;' # Para que se vea ordenado
                }
            )
        },
    }

    def save_model(self, request, obj, form, change):
        # Asigna automáticamente al perfil "Jover Jesus Moreira Mero"
        obj.perfil = DatosPersonales.objects.first()
        super().save_model(request, obj, form, change)

# 3. CONFIGURACIÓN ESPECIAL PARA EL PERFIL
class DatosPersonalesAdmin(admin.ModelAdmin):
    # También aplicamos el selector de fecha aquí para tu nacimiento
    formfield_overrides = {
        models.DateField: {'widget': forms.DateInput(attrs={'type': 'date'})},
    }
    def has_add_permission(self, request):
        return not DatosPersonales.objects.exists()

# 4. REGISTRO DE TODAS LAS SECCIONES
# Ahora todas usarán automáticamente el selector de fecha completo
admin.site.register(DatosPersonales, DatosPersonalesAdmin)
admin.site.register(ExperienciaLaboral, MiHojaDeVidaAdmin)
admin.site.register(Reconocimiento, MiHojaDeVidaAdmin)
admin.site.register(CursoRealizado, MiHojaDeVidaAdmin)
admin.site.register(ProductoAcademico, MiHojaDeVidaAdmin)
admin.site.register(ProductoLaboral, MiHojaDeVidaAdmin)
admin.site.register(VentaGarage, MiHojaDeVidaAdmin)