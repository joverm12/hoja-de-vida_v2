from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

# Limpieza del panel para dejarlo solo con tus modelos
admin.site.unregister(User)
admin.site.unregister(Group)

class DatosPersonalesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Evita que crees más de un perfil personal
        return not DatosPersonales.objects.exists()

class MiHojaDeVidaAdmin(admin.ModelAdmin):
    exclude = ('perfil',) # Oculta el campo perfil para que no lo elijas manualmente
    def save_model(self, request, obj, form, change):
        # Asigna automáticamente el objeto al único perfil existente
        obj.perfil = DatosPersonales.objects.first()
        super().save_model(request, obj, form, change)

# Registro de todas las secciones
admin.site.register(DatosPersonales, DatosPersonalesAdmin)
admin.site.register(ExperienciaLaboral, MiHojaDeVidaAdmin)
admin.site.register(Reconocimiento, MiHojaDeVidaAdmin)
admin.site.register(CursoRealizado, MiHojaDeVidaAdmin)
admin.site.register(ProductoAcademico, MiHojaDeVidaAdmin)
admin.site.register(ProductoLaboral, MiHojaDeVidaAdmin)
admin.site.register(VentaGarage, MiHojaDeVidaAdmin)