from django.db import models
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    puntos = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    club = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre} ({self.club})"

class Estadio(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    capacidad = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombre} con capacidad para {self.capacidad} personas"