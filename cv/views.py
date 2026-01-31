from django.shortcuts import render
from .models import *

def home(request):
    # Obtenemos el perfil (el primero que encuentre)
    perfil = DatosPersonales.objects.first()
    
    # Convertimos el texto de aptitudes en una lista para el HTML
    skills = perfil.aptitudes.split(',') if perfil and perfil.aptitudes else []
    
    # Creamos el contexto con todos los datos filtrados por "activarparaqueseveaenfront"
    context = {
        'p': perfil,
        'skills': skills,
        'experiencias': ExperienciaLaboral.objects.filter(activarparaqueseveaenfront=True),
        'reconocimientos': Reconocimiento.objects.filter(activarparaqueseveaenfront=True),
        'cursos': CursoRealizado.objects.filter(activarparaqueseveaenfront=True),
        # Estas dos líneas son las que activan tus nuevos botones
        'academicos': ProductoAcademico.objects.filter(activarparaqueseveaenfront=True),
        'laborales': ProductoLaboral.objects.filter(activarparaqueseveaenfront=True),
        'garage': VentaGarage.objects.filter(activarparaqueseveaenfront=True),
    }
    
    return render(request, 'index.html', context)