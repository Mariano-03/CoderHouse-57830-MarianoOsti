from django.shortcuts import render

def index(request):
    return render(request, "liga_de_futbol/index.html")