from django.db import models

# Create your models here.

EstadoLibro = [
    ('IN', 'En biblioteca'),
    ('BW', 'Prestado'),
    ('RQ', 'Pedido'),
    ('RV', 'Reservado'),
]

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    tipoPersona = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    numLibros = models.IntegerField()

    #adeudo = models.DoubleFields()

    def _str_(self):
        return "Autor: " + str(self.id) + " " + str(self.nombre)

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmplado = models.IntegerField()

class Material(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipoMaterial = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    anio = models.IntegerField(default=2000)
    status = models.CharField(max_length=2, choices=EstadoLibro, default='En biblioteca')

class Libro(Material):
    editorial = models.CharField(max_length=30)
    portada = models.ImageField(max_length=100, upload_to='fotos_tapa/', default='fotos_tapa/default.png', blank=True)


class Revista(Material):
    pass

class Prestamo (models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    codigo = models.ForeignKey(Material, on_delete=models.CASCADE)
    fechaSalida = models.DateField()
    fechaRegreso = models.DateField()