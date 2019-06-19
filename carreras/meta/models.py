from django.db import models


# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length = 60)
    descripcion = models.CharField(max_length = 200)

class Equipos(models.Model):
    nombre = models.CharField(max_length = 60)
    descripcion = models.CharField(max_length = 200)
    logo = models.CharField(max_length = 20) ## Campo temporal, hasta poner el sistema de subir archivos DurationFile
   

class Carreras(models.Model):
    nombre = models.CharField(max_length = 60)
    fecha_inicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_termino = models.DateTimeField(auto_now=False, auto_now_add=False)
    estatus = models.CharField(max_length = 60)

class Miembros(models.Model):
    equipo = models.ForeignKey(Equipos,on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    edad= models.SmallIntegerField()
    tipo_sangre = models.CharField(max_length=4)
    direccion = models.CharField(max_length=200)
    nss=models.CharField(max_length=100)

class Vueltas(models.Model):
    equipo = models.ForeignKey(Equipos,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carreras,on_delete=models.CASCADE)
    vuelta = models.IntegerField()
    tiempo_total= models.DurationField()
    tiempo_vuelta= models.DurationField()