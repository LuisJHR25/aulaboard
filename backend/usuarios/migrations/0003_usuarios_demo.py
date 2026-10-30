"""Crea usuarios de demostracion para facilitar las pruebas academicas.

Credenciales solo para desarrollo:
- estudiante / Estudiante2026!
- docente / Docente2026!
- coordinador / Coordinador2026!
- admin / AdminAula2026! (superusuario)
"""

from django.contrib.auth.hashers import make_password
from django.db import migrations


USUARIOS_DEMO = (
    {
        "username": "estudiante",
        "first_name": "Estudiante",
        "last_name": "Demo",
        "email": "estudiante@aulaboard.local",
        "password": "Estudiante2026!",
        "rol": "EST",
        "is_staff": False,
        "is_superuser": False,
    },
    {
        "username": "docente",
        "first_name": "Docente",
        "last_name": "Demo",
        "email": "docente@aulaboard.local",
        "password": "Docente2026!",
        "rol": "DOC",
        "is_staff": False,
        "is_superuser": False,
    },
    {
        "username": "coordinador",
        "first_name": "Coordinador",
        "last_name": "Demo",
        "email": "coordinador@aulaboard.local",
        "password": "Coordinador2026!",
        "rol": "COORD",
        "is_staff": False,
        "is_superuser": False,
    },
    {
        "username": "admin",
        "first_name": "Administrador",
        "last_name": "AulaBoard",
        "email": "admin@aulaboard.local",
        "password": "AdminAula2026!",
        "rol": "ADMIN",
        "is_staff": True,
        "is_superuser": True,
    },
)


def crear_usuarios_demo(apps, schema_editor):
    """Crea o actualiza las cuentas de demostracion."""
    Usuario = apps.get_model("usuarios", "Usuario")
    db_alias = schema_editor.connection.alias

    for datos in USUARIOS_DEMO:
        usuario, _ = Usuario.objects.using(db_alias).get_or_create(
            username=datos["username"],
            defaults={
                "first_name": datos["first_name"],
                "last_name": datos["last_name"],
                "email": datos["email"],
                "password": make_password(datos["password"]),
                "rol": datos["rol"],
                "is_staff": datos["is_staff"],
                "is_superuser": datos["is_superuser"],
                "is_active": True,
            },
        )

        # Garantiza credenciales y datos conocidos si la cuenta ya existia.
        usuario.first_name = datos["first_name"]
        usuario.last_name = datos["last_name"]
        usuario.email = datos["email"]
        usuario.password = make_password(datos["password"])
        usuario.rol = datos["rol"]
        usuario.is_staff = datos["is_staff"]
        usuario.is_superuser = datos["is_superuser"]
        usuario.is_active = True
        usuario.save(using=db_alias)


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0002_alter_usuario_rol"),
    ]

    operations = [
        migrations.RunPython(
            crear_usuarios_demo,
            migrations.RunPython.noop,
        ),
    ]
