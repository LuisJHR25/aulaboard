"""Formularios de registro e inicio de sesión."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Usuario


class RegistroForm(UserCreationForm):
    """Registro público de estudiantes.

    El rol se asigna siempre como Estudiante; los demás roles se
    administran desde el panel de administración de Django.
    """

    class Meta:
        """Configuración de campos del formulario de registro."""

        model = Usuario
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "email": "Correo electrónico",
        }

    def __init__(self, *args, **kwargs):
        """Personaliza etiquetas, ayudas y atributos de los campos."""
        super().__init__(*args, **kwargs)

        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

        self.fields["username"].help_text = (
            "Requerido. 150 caracteres o menos. "
            "Puedes usar letras, números y @/./+/-/_."
        )
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmar contraseña"
        self.fields["password1"].help_text = (
            "Mínimo 8 caracteres. No puede ser demasiado similar a tus datos, "
            "una contraseña común ni estar formada solo por números."
        )
        self.fields["password2"].help_text = (
            "Repite la contraseña para confirmarla."
        )

        # Textos de apoyo y atributos de accesibilidad para cada campo.
        placeholders = {
            "username": "Ejemplo: pedro.estudiante",
            "first_name": "Ejemplo: Pedro",
            "last_name": "Ejemplo: Pérez",
            "email": "Ejemplo: pedro@estudiante.com",
            "password1": "Mínimo 8 caracteres",
            "password2": "Repite la contraseña",
        }
        autocomplete = {
            "username": "username",
            "first_name": "given-name",
            "last_name": "family-name",
            "email": "email",
            "password1": "new-password",
            "password2": "new-password",
        }

        for nombre, campo in self.fields.items():
            campo.widget.attrs.setdefault("class", "campo")
            if nombre in placeholders:
                campo.widget.attrs["placeholder"] = placeholders[nombre]
            if nombre in autocomplete:
                campo.widget.attrs["autocomplete"] = autocomplete[nombre]

    def clean_email(self):
        """Evita registrar dos cuentas con el mismo correo."""
        email = self.cleaned_data["email"].strip().lower()
        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Ya existe una cuenta registrada con este correo electrónico."
            )
        return email

    def save(self, commit=True):
        """Guarda la cuenta con rol de estudiante y correo normalizado."""
        usuario = super().save(commit=False)
        usuario.rol = Usuario.Rol.ESTUDIANTE
        usuario.email = usuario.email.lower()
        if commit:
            usuario.save()
        return usuario


class LoginForm(AuthenticationForm):
    """Formulario de inicio de sesión con etiquetas en español."""

    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(
            attrs={
                "class": "campo",
                "autofocus": True,
                "placeholder": "Tu nombre de usuario",
                "autocomplete": "username",
            }
        ),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "campo",
                "placeholder": "Tu contraseña",
                "autocomplete": "current-password",
            }
        ),
    )
