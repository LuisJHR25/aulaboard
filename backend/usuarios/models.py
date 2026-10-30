"""Modelos de usuarios y roles de AulaBoard."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuario del sistema con un rol academico."""

    class Rol(models.TextChoices):
        """Roles disponibles para los usuarios del sistema."""

        ADMINISTRADOR = "ADMIN", "Administrador"
        COORDINADOR = "COORD", "Coordinador Académico"
        DOCENTE = "DOC", "Docente"
        ESTUDIANTE = "EST", "Estudiante"

    rol = models.CharField(
        "Rol",
        max_length=10,
        choices=Rol.choices,
        default=Rol.ESTUDIANTE,
        help_text="Define los permisos y el panel al que accede el usuario.",
    )

    class Meta:
        """Metadatos del modelo en el panel de administración."""

        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        """Devuelve el nombre completo y el rol del usuario."""
        nombre = self.get_full_name() or self.username
        return f"{nombre} ({self.get_rol_display()})"

    # Propiedades de conveniencia usadas por las plantillas y las vistas.
    @property
    def es_administrador(self):
        return self.rol == self.Rol.ADMINISTRADOR

    @property
    def es_coordinador(self):
        return self.rol == self.Rol.COORDINADOR

    @property
    def es_docente(self):
        return self.rol == self.Rol.DOCENTE

    @property
    def es_estudiante(self):
        return self.rol == self.Rol.ESTUDIANTE
