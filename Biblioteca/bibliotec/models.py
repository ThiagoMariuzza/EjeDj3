from django.db import models

# Create your models here.

class Persona(models.Models):
    id = models.AutoField(primary_key=True)
    tipoPersona = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.ImageField()
    numLibros = models.ImageField()
    adeudo = models.DoubleFields()

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmplado = models.IntegerField()

class Material(models.Models):
    codigo = models.AutoField(primary_key=True)
    tipoMaterial = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    anio = models.IntegerField
    status = models.CharField(max_length=30)

class Libro(Material):
    editorial = models.CharField(max_length=30)

class Revista(Material):
    pass

class Prestamo (models.Models):
    idPrestamo = models.AutoField(primary_key=True)
    id = models.ForeignKey(Persona, on_delete=models.CASCADE())
    codigo = models.ForeignKey(Material, on_delete=models.CASCADE())
    fechaSalida = models.DateField()
    fechaRegreso = models.DateField()