from django.contrib import admin
from .models import Equipo, Jugador, Estadio, Clasificacion, UsuarioPremium

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puntos')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'club')
    search_fields = ('nombre', 'apellido', 'club')
    ordering = ('club', 'apellido', 'nombre')

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    
@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('equipo__nombre', 'equipo__puntos')
    search_fields = ('equipo__nombre',)
    ordering = ('-equipo__puntos', 'equipo__nombre')

admin.site.register(UsuarioPremium)