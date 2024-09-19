from django.db import models
from django.contrib.auth.models import User
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    puntos = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    club = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre} ({self.club})"

class Estadio(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    capacidad = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombre} con capacidad para {self.capacidad} personas"
    
class Clasificacion(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipo.nombre} {self.equipo.puntos}"
    
class UsuarioPremium(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")
    celular = models.CharField(max_length=30, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return self.usuario.username