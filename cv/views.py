from django.shortcuts import render
from .models import *

def home(request):
    # Obtenemos el perfil
    perfil = DatosPersonales.objects.first()
    
    # LIMPIEZA: Eliminamos espacios al inicio/final para quitar el "espaciado de siempre"
    if perfil and perfil.sobre_mi:
        perfil.sobre_mi = perfil.sobre_mi.strip()
    
    # Convertimos aptitudes en lista y limpiamos espacios de cada una
    skills = [s.strip() for s in perfil.aptitudes.split(',')] if perfil and perfil.aptitudes else []
    
    # Contexto con filtros activos
    context = {
        'p': perfil,
        'skills': skills,
        'experiencias': ExperienciaLaboral.objects.filter(activarparaqueseveaenfront=True),
        'reconocimientos': Reconocimiento.objects.filter(activarparaqueseveaenfront=True),
        'cursos': CursoRealizado.objects.filter(activarparaqueseveaenfront=True),
        'academicos': ProductoAcademico.objects.filter(activarparaqueseveaenfront=True),
        'laborales': ProductoLaboral.objects.filter(activarparaqueseveaenfront=True),
        'garage': VentaGarage.objects.filter(activarparaqueseveaenfront=True),
    }
    
    return render(request, 'index.html', context)