"""Rutas de autenticacion y paneles de la app usuarios."""

from django.urls import path

from . import views

urlpatterns = [
    # Rutas públicas y de autenticación.
    path("", views.home, name="home"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.iniciar_sesion, name="login"),
    path("logout/", views.cerrar_sesion, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # Paneles protegidos según el rol del usuario.
    path(
        "dashboard/estudiante/",
        views.dashboard_estudiante,
        name="dashboard_estudiante",
    ),
    path(
        "dashboard/docente/",
        views.dashboard_docente,
        name="dashboard_docente",
    ),
    path(
        "panel/coordinador/",
        views.panel_coordinador,
        name="panel_coordinador",
    ),
    path(
        "panel/administrador/",
        views.panel_administrador,
        name="panel_administrador",
    ),
]
