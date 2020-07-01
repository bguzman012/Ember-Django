from django.db import models

# Create your models here.
class Estudiante(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)

    class Meta:
        db_table = "estudiantes"
        verbose_name_plural = "estudiantes"

    class JSONAPIMeta:
        resource_name = "estudiantes"

class Representante(models.Model):
    
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    
    class Meta:
        db_table = "representantes"
        verbose_name_plural = "representantes"


    class JSONAPIMeta:
        resource_name = "representantes"