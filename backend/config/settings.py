"""Configuracion minima de Django para AulaBoard."""

import os
from pathlib import Path

# Directorio raíz del proyecto, usado para construir rutas internas.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de seguridad y hosts permitidos.
# Los valores por defecto están pensados para desarrollo local.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-aulaboard-dev",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")
    if host.strip()
]

# Aplicaciones propias y de terceros que habilitan la funcionalidad del proyecto.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "usuarios",
]

# Middleware de seguridad, sesiones, CORS y mensajes.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# Motor de plantillas y procesadores compartidos por las vistas.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Punto de entrada para servidores WSGI.
WSGI_APPLICATION = "config.wsgi.application"

# Base de datos local; SQLite evita servicios externos durante el desarrollo.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Modelo de usuario personalizado y rutas de autenticación.
AUTH_USER_MODEL = "usuarios.Usuario"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "home"

# Reglas mínimas de seguridad para las contraseñas de los usuarios.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Idioma y zona horaria usados por Django.
LANGUAGE_CODE = "es"

TIME_ZONE = "America/Caracas"

USE_I18N = True

USE_TZ = True

# Archivos estáticos servidos durante el desarrollo.
STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Orígenes permitidos para el frontend Vite y peticiones protegidas.
CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "DJANGO_CORS_ALLOWED_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
