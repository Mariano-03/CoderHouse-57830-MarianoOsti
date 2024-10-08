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
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from liga_de_futbol import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login', LoginView.as_view(template_name="liga_de_futbol/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="liga_de_futbol/logout.html"), name="logout"),
    path('register', views.Register.as_view(), name="register"),
    path('profile', views.Profile.as_view(), name="profile"),
    path('about', views.about, name="about"),
    path('equipo/list/', login_required(views.equipo_list), name="equipo_list"),
    path('equipo/create/', login_required(views.equipo_create), name="equipo_create"),
    path('equipo/update/<int:pk>', login_required(views.equipo_update), name="equipo_update"),
    path('equipo/delete/<int:pk>', login_required(views.equipo_delete), name="equipo_delete"),
    path('jugador/list/', login_required(views.jugador_list), name="jugador_list"),
    path('jugador/create/', login_required(views.jugador_create), name="jugador_create"),
    path('jugador/detail/<int:pk>', login_required(views.jugador_detail), name="jugador_detail"),
    path('jugador/update/<int:pk>', login_required(views.jugador_update), name="jugador_update"),
    path('jugador/delete/<int:pk>', login_required(views.jugador_delete), name="jugador_delete"),
    path('estadio/list/', login_required(views.estadio_list), name="estadio_list"),
    path('estadio/create/', login_required(views.estadio_create), name="estadio_create"),
    path('estadio/detail/<int:pk>', login_required(views.estadio_detail), name="estadio_detail"),
    path('estadio/update/<int:pk>', login_required(views.estadio_update), name="estadio_update"),
    path('estadio/delete/<int:pk>', login_required(views.estadio_delete), name="estadio_delete"),
    path('clasificacion/', login_required(views.clasificacion), name="clasificacion")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )