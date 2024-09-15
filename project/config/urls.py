"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from liga_de_futbol import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('equipo/list/', views.equipo_list, name="equipo_list"),
    path('equipo/create/', views.equipo_create, name="equipo_create"),
    path('equipo/update/<int:pk>', views.equipo_update, name="equipo_update"),
    path('jugador/list/', views.jugador_list, name="jugador_list"),
    path('jugador/create/', views.jugador_create, name="jugador_create"),
    path('jugador/detail/<int:pk>', views.jugador_detail, name="jugador_detail"),
    path('jugador/update/<int:pk>', views.jugador_update, name="jugador_update"),
    path('estadio/list/', views.estadio_list, name="estadio_list"),
    path('estadio/create/', views.estadio_create, name="estadio_create"),
    path('estadio/detail/<int:pk>', views.estadio_detail, name="estadio_detail"),
    path('estadio/update/<int:pk>', views.estadio_update, name="estadio_update"),
    path('clasificacion/', views.clasificacion, name="clasificacion")
]
