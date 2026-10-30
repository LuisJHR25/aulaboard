"""Rutas principales del proyecto AulaBoard."""

from django.contrib import admin
from django.urls import include, path

# Textos visibles en el panel de administración de Django.
admin.site.site_header = "AulaBoard - Administración"
admin.site.site_title = "AulaBoard"
admin.site.index_title = "Panel de administración"

urlpatterns = [
    # Panel administrativo de Django.
    path("admin/", admin.site.urls),
    # Rutas públicas, de autenticación y paneles de la aplicación.
    path("", include("usuarios.urls")),
]
