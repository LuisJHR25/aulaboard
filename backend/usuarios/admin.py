"""Configuracion del admin para usuarios y roles."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Administracion de usuarios con su rol de AulaBoard."""

    # Columnas y filtros que facilitan la gestión de usuarios.
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "rol",
        "is_staff",
        "is_active",
    )
    list_filter = ("rol", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    # El rol se añade a los formularios estándar del administrador.
    fieldsets = UserAdmin.fieldsets + (
        ("Rol en AulaBoard", {"fields": ("rol",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Rol en AulaBoard", {"fields": ("rol",)}),
    )
