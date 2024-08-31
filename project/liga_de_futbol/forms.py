from django import forms
from .models import Equipo, Jugador, Estadio

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = "__all__"
        widgets = {"fecha_nacimiento": forms.DateInput(attrs={"type": "date"})}

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = "__all__"