from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from cloudinary.models import CloudinaryField

# 1. VALIDACIÓN UNIVERSAL DE FECHA
def validar_fecha_no_futura(value):
    if value > timezone.now().date():
        raise ValidationError('¡Cuidado! No puedes poner una fecha futura.')

# 2. DATOS PERSONALES
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

# 3. EXPERIENCIA LABORAL (Campos de empresa opcionales)
class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50, null=True, blank=True)
    emailempresa = models.CharField(max_length=100, null=True, blank=True)
    sitiowebempresa = models.CharField(max_length=100, null=True, blank=True)
    nombrecontactoempresarial = models.CharField(max_length=100, null=True, blank=True)
    telefonocontactoempresarial = models.CharField(max_length=60, null=True, blank=True)
    fechainiciogestion = models.DateField(validators=[validar_fecha_no_futura])
    fechafingestion = models.DateField(null=True, blank=True, validators=[validar_fecha_no_futura])
    descripcionfunciones = models.CharField(max_length=100)
    rutacertificado = CloudinaryField('documento', folder='experiencia/', resource_type='raw', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

# 4. RECONOCIMIENTOS (Con descripción para cuando no hay PDF)
class Reconocimiento(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrereconocimiento = models.CharField(max_length=100)
    institucionqueotorga = models.CharField(max_length=100)
    fechareconocimiento = models.DateField(validators=[validar_fecha_no_futura])
    descripcion = models.TextField(blank=True, null=True) 
    comprobante_archivo = CloudinaryField('documento', folder='reconocimientos/', resource_type='raw', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

# 5. CURSOS REALIZADOS
class CursoRealizado(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrerecurso = models.CharField(max_length=100)
    fechainicio = models.DateField(validators=[validar_fecha_no_futura])
    fechafin = models.DateField(validators=[validar_fecha_no_futura])
    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100, null=True, blank=True)
    telefonocontactoauspicia = models.CharField(max_length=60, null=True, blank=True)
    emailempresapatrocinadora = models.CharField(max_length=60, null=True, blank=True)
    rutacertificado = CloudinaryField('documento', folder='cursos/', resource_type='raw', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    def __str__(self): return self.nombrerecurso

# 6. PRODUCTOS ACADÉMICOS
class ProductoAcademico(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)

# 7. PRODUCTOS LABORALES
class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField(validators=[validar_fecha_no_futura])
    descripcion = models.TextField(blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

# 8. VENTA GARAGE
class VentaGarage(models.Model):
    ESTADO_CHOICES = [('Bueno', 'Bueno'), ('Regular', 'Regular')]
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40, choices=ESTADO_CHOICES, default='Bueno')
    valordelbien = models.DecimalField(max_digits=10, decimal_places=2)
    foto_producto = CloudinaryField('imagen', folder='garage/', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)