from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Estadio, Clasificacion
from .forms import EquipoForm, JugadorForm, EstadioForm

def index(request):
    return render(request, "liga_de_futbol/index.html")

def equipo_list(request):
    query = request.GET.get("q")
    if query:
        equipos = Equipo.objects.filter(nombre__icontains=query)
    else:
        equipos = Equipo.objects.all().order_by('nombre')
    context = {"object_list": equipos}
    return render(request, "liga_de_futbol/equipo_list.html", context)

def equipo_create(request):
    if request.method == "GET":
        form = EquipoForm()
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipo_list")
    return render(request, "liga_de_futbol/equipo_create.html", {"form": form})

def equipo_update(request, pk):
    query = Equipo.objects.get(id=pk)
    if request.method == "GET":
        form = EquipoForm(instance=query)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("equipo_list")
    return render(request, "liga_de_futbol/equipo_create.html", {"form": form})

def equipo_delete(request, pk):
    query = Equipo.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect("equipo_list")
    return render(request, "liga_de_futbol/equipo_confirm_delete.html", {"object": query})

def jugador_list(request):
    query = request.GET.get("q")
    if query:
        jugadores = Jugador.objects.filter(nombre__icontains=query)
    else:
        jugadores = Jugador.objects.all()
    context = {"object_list": jugadores}
    return render(request, "liga_de_futbol/jugador_list.html", context)

def jugador_create(request):
    if request.method == "GET":
        form = JugadorForm()
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jugador_list")
    return render(request, "liga_de_futbol/jugador_create.html", {"form": form})

def jugador_detail(request, pk: int):
    query = Jugador.objects.get(id=pk)
    context = {"object": query}
    return render(request, "liga_de_futbol/jugador_detail.html", context)

def jugador_update(request, pk):
    query = Jugador.objects.get(id=pk)
    if request.method == "GET":
        form = JugadorForm(instance=query)
    if request.method == "POST":
        form = JugadorForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("jugador_list")
    return render(request, "liga_de_futbol/jugador_create.html", {"form": form})

def jugador_delete(request, pk):
    query = Jugador.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect("jugador_list")
    return render(request, "liga_de_futbol/jugador_confirm_delete.html", {"object": query})

def estadio_list(request):
    estadios = Estadio.objects.all()
    context = {"object_list": estadios}
    return render(request, "liga_de_futbol/estadio_list.html", context)

def estadio_create(request):
    if request.method == "GET":
        form = EstadioForm()
    if request.method == "POST":
        form = EstadioForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("estadio_list")
    return render(request, "liga_de_futbol/estadio_create.html", {"form": form})

def estadio_detail(requqest, pk: int):
    query = Estadio.objects.get(id=pk)
    context = {"object": query}
    return render(requqest, "liga_de_futbol/estadio_detail.html", context)

def estadio_update(request, pk):
    query = Estadio.objects.get(id=pk)
    if request.method == "GET":
        form = EstadioForm(instance=query)
    if request.method == "POST":
        form = EstadioForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("estadio_list")
    return render(request, "liga_de_futbol/estadio_create.html", {"form": form})

def estadio_delete(request, pk):
    query = Estadio.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect("estadio_list")
    return render(request, "liga_de_futbol/estadio_confirm_delete.html", {"object": query})

def clasificacion(request):
    clasificacion = Equipo.objects.all().order_by('-puntos')
    context = {"object_list": clasificacion}
    return render(request, "liga_de_futbol/clasificacion.html", context)