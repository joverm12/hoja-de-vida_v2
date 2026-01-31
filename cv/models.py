from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from cloudinary.models import CloudinaryField

def validar_fecha_no_futura(value):
    if value > timezone.now().date():
        raise ValidationError('¡Cuidado! No puedes poner una fecha futura.')

class DatosPersonales(models.Model):
    foto = CloudinaryField('imagen', folder='perfil/', null=True, blank=True)
    sobre_mi = models.TextField()
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField(validators=[validar_fecha_no_futura])
    numerocedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1, choices=[('H', 'Hombre'), ('M', 'Mujer')])
    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6, blank=True)
    telefonofijo = models.CharField(max_length=15)
    direcciondomiciliaria = models.CharField(max_length=100)
    sitioweb = models.URLField(max_length=100, blank=True)
    universidad = models.CharField(max_length=100, default="ULEAM")
    periodo_u = models.CharField(max_length=50, default="Mayo 2024 - En curso")
    bachillerato_status = models.CharField(max_length=100, default="Bachillerato - Completo")
    certificado_bachiller_pdf = CloudinaryField('documento', folder='certificados/', resource_type='raw', null=True, blank=True)
    aptitudes = models.TextField(help_text="Separa por comas")

    def __str__(self): return f"{self.nombres} {self.apellidos}"

class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField(null=True, blank=True)
    actividadesrealizadas = models.TextField()
    activarparaqueseveaenfront = models.BooleanField(default=True)

class Reconocimiento(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrereconocimiento = models.CharField(max_length=100)
    institucionqueotorga = models.CharField(max_length=100)
    fechareconocimiento = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    comprobante_archivo = CloudinaryField('documento', folder='reconocimientos/', resource_type='raw', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

class CursoRealizado(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrecurso = models.CharField(max_length=150)
    nombreinstitucion = models.CharField(max_length=100)
    numerohoras = models.IntegerField()
    certificado_pdf = CloudinaryField('documento', folder='cursos/', resource_type='raw', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

class ProductoAcademico(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.TextField()
    activarparaqueseveaenfront = models.BooleanField(default=True)

class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

class VentaGarage(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40)
    valordelbien = models.DecimalField(max_digits=10, decimal_places=2)
    foto_producto = CloudinaryField('imagen', folder='garage/', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)