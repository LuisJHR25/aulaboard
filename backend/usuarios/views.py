"""Vistas de autenticacion y paneles por rol."""

from functools import wraps

from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistroForm
from .models import Usuario


def rol_requerido(rol):
    """Permite el acceso solo a usuarios con el rol indicado."""

    def decorador(vista):
        """Envuelve la vista con autenticación y validación de rol."""

        @login_required
        @wraps(vista)
        def envoltura(request, *args, **kwargs):
            """Comprueba el rol antes de ejecutar la vista protegida."""
            if request.user.is_superuser or request.user.rol == rol:
                return vista(request, *args, **kwargs)

            messages.error(request, "No tienes permiso para acceder a ese panel.")
            return redirect("dashboard")

        return envoltura

    return decorador


def home(request):
    """Pagina publica de inicio."""
    return render(request, "home.html")


def registro(request):
    """Registro publico de estudiantes."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegistroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Cuenta creada correctamente. Ya puedes iniciar sesión.",
        )
        return redirect("login")

    return render(request, "usuarios/registro.html", {"form": form})


def iniciar_sesion(request):
    """Inicio de sesion con nombre de usuario y contrasena."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        auth_login(request, form.get_user())
        return redirect("dashboard")

    return render(request, "usuarios/login.html", {"form": form})


@login_required
def cerrar_sesion(request):
    """Muestra la confirmacion por GET y cierra la sesion por POST."""
    if request.method == "POST":
        auth_logout(request)
        return redirect("home")

    return render(request, "usuarios/logout.html")


@login_required
def dashboard(request):
    """Redirige al panel correspondiente segun el rol del usuario."""
    # Cada rol tiene su propio panel; el mapa evita condicionales repetidos.
    destinos = {
        Usuario.Rol.ESTUDIANTE: "dashboard_estudiante",
        Usuario.Rol.DOCENTE: "dashboard_docente",
        Usuario.Rol.COORDINADOR: "panel_coordinador",
        Usuario.Rol.ADMINISTRADOR: "panel_administrador",
    }
    return redirect(destinos.get(request.user.rol, "home"))


@rol_requerido(Usuario.Rol.ESTUDIANTE)
def dashboard_estudiante(request):
    """Muestra el panel de anuncios del estudiante."""
    return render(request, "usuarios/dashboard_estudiante.html")


@rol_requerido(Usuario.Rol.DOCENTE)
def dashboard_docente(request):
    """Muestra el panel de secciones del docente."""
    return render(request, "usuarios/dashboard_docente.html")


@rol_requerido(Usuario.Rol.COORDINADOR)
def panel_coordinador(request):
    """Muestra el panel de gestión académica de coordinación."""
    return render(request, "usuarios/panel_coordinador.html")


@rol_requerido(Usuario.Rol.ADMINISTRADOR)
def panel_administrador(request):
    """Muestra el panel de administración del sistema."""
    # Totales globales y conteos de usuarios activos por rol.
    metricas = Usuario.objects.aggregate(
        total=Count("id"),
        activos=Count("id", filter=Q(is_active=True)),
        estudiantes_activos=Count(
            "id",
            filter=Q(is_active=True, rol=Usuario.Rol.ESTUDIANTE),
        ),
        docentes_activos=Count(
            "id",
            filter=Q(is_active=True, rol=Usuario.Rol.DOCENTE),
        ),
        coordinadores_activos=Count(
            "id",
            filter=Q(is_active=True, rol=Usuario.Rol.COORDINADOR),
        ),
        administradores_activos=Count(
            "id",
            filter=Q(is_active=True, rol=Usuario.Rol.ADMINISTRADOR),
        ),
    )
    return render(
        request,
        "usuarios/panel_administrador.html",
        {"metricas": metricas},
    )
