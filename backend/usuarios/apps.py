"""Configuración de la aplicación de usuarios y roles."""

from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    """Define los valores base de la aplicación usuarios."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "usuarios"
    verbose_name = "Usuarios y roles"
