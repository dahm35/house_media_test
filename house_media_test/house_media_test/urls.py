"""house_media_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from apps.turno.views import TurnoList, TurnoCreateView, TurnoUpdateView, TurnoDeleteView, TurnosPendientesView, TurnosStaff
from apps.usuario.views import UserList, UserCreateView, UserUpdateView, UserDeleteView, UserAnonymousView
from apps.turno.TurnosCreados import TurnosCreados
from apps.usuario.ExistenciaUsuario import ExistenciaUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='index.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name = 'logout'),
    
    path('turnos/', TurnoList.as_view(), name='turnos'),
    path('crear_turno/', TurnoCreateView.as_view(), name='crear_turno'),
    path('editar_turno/<int:pk>', TurnoUpdateView.as_view(), name='editar_turno'),
    path('eliminar_turno/<int:pk>', TurnoDeleteView.as_view(), name='eliminar_turno'),
    path('turnos_pendientes/', TurnosPendientesView.as_view(), name='turnos_pendientes'),
    path('turnos_staff/', TurnosStaff.as_view(), name='turnos_staff'),

    path('usuarios/', UserList.as_view(), name='usuarios'),
    path('crear_usuario/', UserCreateView.as_view(), name='crear_usuario'),
    path('editar_usuario/<int:pk>', UserUpdateView.as_view(), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>', UserDeleteView.as_view(), name='eliminar_usuario'),
    path('usuarios_anonimo/', UserAnonymousView.as_view(), name='usuarios_anonimo'),
    
    path('turnos_creados/', TurnosCreados.as_view(), name='turnos_creados'),
    path('existe_usuario/<int:pk>', ExistenciaUsuario.as_view(), name='existe_usuario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)