# AulaBoard

AulaBoard es una aplicación web académica para centralizar los anuncios de la carrera de Ingeniería en Informática. El proyecto organiza la información por anuncios generales, materias, secciones y períodos académicos, con acceso diferenciado para estudiantes, docentes, coordinación y administración.

La versión actual implementa la base de autenticación, los roles y los paneles iniciales por rol. La interfaz se sirve con plantillas de Django y el frontend Vite se mantiene como base separada para una integración posterior.

## Contenido

- [Descripción](#descripcion)
- [Stack tecnológico](#stack-tecnologico)
- [Metodología en V: rama descendente](#metodologia-en-v-rama-descendente)
- [Checklist B.1-B.8](#checklist-b1-b8)
- [Arquitectura](#arquitectura)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación y ejecución](#instalacion-y-ejecucion)
- [Usuarios de prueba](#usuarios-de-prueba)
- [Rutas principales](#rutas-principales)
- [Roles y permisos](#roles-y-permisos)
- [Estado actual y limitaciones](#estado-actual-y-limitaciones)
- [Roadmap](#roadmap)
- [Notas de seguridad](#notas-de-seguridad)

## Descripción <a name="descripcion"></a>

### Propósito

AulaBoard busca evitar que los anuncios académicos se dispersen entre mensajería, correos y grupos informales. La aplicación propone un espacio único donde:

- La coordinación publica comunicados generales para toda la carrera.
- Los docentes publican avisos en las secciones que tienen asignadas.
- Los estudiantes consultan anuncios generales y de las secciones a las que se unen.
- La administración gestiona usuarios, roles y la configuración del sistema.

### Alcance de esta versión

La base implementada incluye:

- Página pública de inicio.
- Registro público de estudiantes.
- Inicio y cierre de sesión.
- Usuario personalizado con rol académico.
- Redirección al panel correspondiente según el rol.
- Paneles por rol con vistas previas y estados de módulos en preparación.
- Panel administrativo con métricas reales de usuarios totales, activos y activos por rol.
- Administración de usuarios y roles desde Django Admin.
- Interfaz adaptable con tema claro y oscuro.

Los anuncios, períodos académicos, materias, secciones, asignaciones docentes, inscripciones de estudiantes y búsqueda avanzada forman parte de las siguientes fases del proyecto.

## Stack tecnológico <a name="stack-tecnologico"></a>

| Componente | Tecnología | Uso en el proyecto |
|---|---|---|
| Backend | Python 3.12 + Django 5.2 | Autenticación, vistas, formularios, rutas y administración |
| Base de datos | SQLite | Persistencia local en `backend/db.sqlite3` |
| Frontend | Vite 8 + JavaScript + HTML + CSS | Base del frontend y servidor de desarrollo |
| Estilos | CSS personalizado | Interfaz adaptable, componentes y tema claro/oscuro |
| Contenedores | Docker + Docker Compose | Entorno reproducible de backend y frontend |
| Dependencias backend | `requirements.txt` | Django y `django-cors-headers` |

El frontend Vite todavía no consume una API del backend. Las pantallas visibles de AulaBoard se renderizan desde Django; el servicio Vite queda preparado para la integración futura.

## Metodología en V: rama descendente <a name="metodologia-en-v-rama-descendente"></a>

El proyecto sigue la rama descendente de la metodología en V. Cada etapa descompone el problema y produce insumos concretos para la siguiente, hasta llegar al punto de inflexión en la codificación.

```text
Análisis de requisitos
        |
        v
Análisis del sistema
        |
        v
Diseño de software y arquitectura
        |
        v
Diseño de módulos
        |
        v
Punto de inflexión: CODIFICACIÓN
```

### 1. Análisis de requisitos

Esta etapa define qué debe resolver AulaBoard y quiénes interactúan con el sistema.

**Actores identificados:**

- **Visitante:** puede consultar la página de inicio, registrarse o iniciar sesión.
- **Estudiante:** consulta anuncios generales y de sus secciones; se registra públicamente con ese rol.
- **Docente:** publica y consulta anuncios de las secciones que tenga asignadas.
- **Coordinador académico:** administra períodos, materias, secciones, asignaciones y anuncios generales.
- **Administrador:** gestiona usuarios, roles y la configuración general del sistema.

**Necesidades principales:**

- Centralizar anuncios académicos en una sola aplicación.
- Separar los anuncios generales de los anuncios por materia y sección.
- Restringir la publicación de anuncios según el rol y las secciones asignadas.
- Permitir que los estudiantes se unan libremente a las secciones que desean seguir.
- Filtrar anuncios por categoría, materia, sección, fecha o palabra clave.
- Mantener una interfaz clara y accesible para distintos dispositivos.

**Requisitos funcionales de la base actual:**

- Registro público de estudiantes.
- Inicio y cierre de sesión.
- Asignación de un rol a cada usuario.
- Redirección automática al panel correspondiente.
- Protección de paneles según el rol.
- Administración de usuarios desde Django Admin.

### 2. Análisis del sistema

Esta etapa traduce las necesidades en flujos y responsabilidades dentro del sistema.

**Flujo de autenticación:**

1. El visitante se registra o inicia sesión.
2. Al registrarse, la cuenta se crea con el rol **Estudiante**.
3. Al iniciar sesión, el sistema consulta el rol del usuario.
4. El usuario es redirigido a su panel correspondiente.
5. Si intenta abrir un panel de otro rol, el sistema lo devuelve a su propio panel con un mensaje de error.

**Flujo por rol:**

- El estudiante accede a su panel de anuncios y secciones.
- El docente accede a su panel de secciones asignadas y publicación de anuncios.
- El coordinador accede a la gestión académica y a los anuncios generales.
- El administrador accede al panel administrativo y a Django Admin.

**Decisión de diseño:** los roles no se eligen durante el registro público. Los roles de docente, coordinador y administrador se asignan desde Django Admin para evitar que un visitante se otorgue privilegios.

### 3. Diseño de software y arquitectura

AulaBoard utiliza una arquitectura web monolítica con Django para el backend y el renderizado de plantillas.

**Componentes principales:**

- **Navegador:** envía solicitudes y recibe páginas HTML.
- **Django:** procesa rutas, formularios, autenticación, permisos y plantillas.
- **SQLite:** almacena usuarios, roles y datos del sistema.
- **Django Admin:** permite administrar usuarios y roles.
- **Vite:** servicio independiente para el desarrollo del frontend futuro.
- **Docker Compose:** orquesta backend y frontend en un entorno reproducible.

**Decisiones de arquitectura:**

- Usuario personalizado basado en `AbstractUser` para incorporar el rol académico.
- Aplicación `usuarios` para concentrar autenticación, roles y paneles.
- Vistas basadas en funciones y un decorador reutilizable para restringir el acceso por rol.
- Plantillas organizadas por responsabilidad: autenticación y paneles.
- Servicios separados de backend y frontend para facilitar el desarrollo y la futura integración por API.
- SQLite como base de datos de desarrollo por simplicidad y portabilidad.

### 4. Diseño de módulos

El backend se organiza en un proyecto de configuración y una aplicación principal.

**Proyecto `config`:**

- `settings.py`: configuración de Django, base de datos, plantillas, autenticación, CORS y variables de entorno.
- `urls.py`: punto de entrada de las rutas y del panel administrativo.
- `wsgi.py` y `asgi.py`: interfaces de despliegue del proyecto.

**Aplicación `usuarios`:**

- `models.py`: modelo `Usuario`, roles y propiedades de comprobación.
- `forms.py`: formulario de registro y formulario de inicio de sesión.
- `views.py`: inicio, registro, login, logout, redirección y paneles protegidos.
- `urls.py`: rutas de autenticación y paneles.
- `admin.py`: administración de usuarios con su rol.
- `migrations/`: estructura de la base de datos y cuentas de demostración.
- `templates/`: páginas de inicio, autenticación y paneles por rol.
- `static/css/estilos.css`: estilos globales, componentes y temas.

**Módulos previstos para las siguientes fases:**

- Períodos académicos.
- Materias y secciones.
- Asignaciones de docentes a secciones.
- Inscripción de estudiantes a secciones.
- Anuncios y categorías.
- Búsqueda y filtros.
- Notificaciones.

### 5. Punto de inflexión: codificación

La codificación integra las decisiones anteriores en una aplicación funcional. En esta etapa se construyeron:

- El proyecto Django y la aplicación `usuarios`.
- El modelo de usuario personalizado con roles.
- El registro público de estudiantes.
- El inicio y cierre de sesión.
- La redirección y protección de paneles por rol.
- Las plantillas iniciales para cada rol.
- La configuración de Django Admin.
- La interfaz adaptable con tema claro y oscuro.
- El entorno de desarrollo con Docker Compose.

La implementación actual corresponde a la base de autenticación y roles. Las funcionalidades académicas se incorporarán de forma incremental en las siguientes fases.

## Checklist B.1-B.8 <a name="checklist-b1-b8"></a>

Las siguientes condiciones estructuran el inicio de la fase de codificación. Cada una se justifica por su aporte al proyecto.

| Condición | Justificación |
|---|---|
| **B.1. Stack de desarrollo** | Python, Django, Vite y Docker están definidos como componentes del proyecto. Los Dockerfiles, `requirements.txt` y `package.json` permiten reconstruir el entorno sin instalar todo manualmente en cada equipo. |
| **B.2. Entorno virtual con Docker** | Docker Compose separa backend y frontend, conserva las dependencias dentro de cada servicio y evita conflictos con el entorno del sistema anfitrión. Los volúmenes mantienen el código sincronizado durante el desarrollo. |
| **B.3. Control de versiones** | Un historial de cambios permite conservar el avance, comparar modificaciones y recuperar versiones anteriores. La separación entre backend, frontend y configuración facilita organizar el proyecto por áreas. |
| **B.4. Django y librerías** | Django proporciona autenticación, formularios, rutas, plantillas y administración. `django-cors-headers` queda configurado para permitir la comunicación con el frontend Vite cuando se integre la API. |
| **B.5. Backend estructurado** | El proyecto `config` concentra la configuración y la aplicación `usuarios` agrupa autenticación, roles y paneles. Esta separación mantiene el código ordenado y deja espacio para futuras aplicaciones académicas. |
| **B.6. Módulo de registro e inicio de sesión** | La aplicación `usuarios` incluye registro, inicio y cierre de sesión, validación de correo duplicado, asignación automática del rol Estudiante y redirección según el rol. |
| **B.7. Django Admin** | El modelo `Usuario` está registrado con campos de búsqueda, filtros y el rol editable. Esto permite crear docentes, coordinadores y administradores sin modificar la base de datos manualmente. |
| **B.8. Vistas por roles** | Existen paneles para estudiante, docente, coordinación y administración. El decorador `rol_requerido` impide que un usuario abra el panel de otro rol y redirige a su panel correspondiente. |

## Arquitectura

```text
Navegador
    |
    v
Django (rutas, formularios, vistas y plantillas)
    |
    +--> Autenticación y roles
    |
    +--> Paneles por rol
    |
    +--> Django Admin
    |
    v
SQLite (backend/db.sqlite3)

Docker Compose
    ├── backend  -> Django en el puerto 8000
    └── frontend -> Vite en el puerto 5173
```

El backend es la aplicación principal y sirve las pantallas mediante plantillas. El frontend Vite se ejecuta de forma independiente y todavía no está conectado a una API de AulaBoard.

## Estructura del proyecto

```text
aulaboard/
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── usuarios/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── usuarios/
│   ├── static/
│   │   └── css/
│   │       └── estilos.css
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   ├── index.html
│   └── package.json
├── docker-compose.yml
└── README.md
```

## Instalación y ejecución <a name="instalacion-y-ejecucion"></a>

### Requisitos

- Docker Engine con Docker Compose v2.
- Puertos `8000` y `5173` disponibles.
- Opcional para ejecución local: Python 3.12 y Node.js compatible con Vite 8.

### Clona/Descarga el Repositorio

```bash
cd aulaboard
docker compose up --build
```

En el primer arranque, el servicio `backend` aplica las migraciones automáticamente y crea las cuentas de demostración. Después inicia Django en el puerto `8000`; Vite se inicia en el puerto `5173`.

### Direcciones de acceso

| Servicio | Dirección |
|---|---|
| Aplicación AulaBoard | `http://localhost:8000/` |
| Django Admin | `http://localhost:8000/admin/` |
| Frontend Vite | `http://localhost:5173/` |

### Detener los servicios

```bash
docker compose down
```

La base de datos SQLite se guarda en `backend/db.sqlite3` y se conserva al detener los contenedores.

### Ver registros del backend

```bash
docker compose logs -f backend
```

### Aplicar migraciones manualmente

```bash
docker compose exec backend python manage.py migrate
```

### Crear un superusuario adicional

```bash
docker compose exec backend python manage.py createsuperuser
```

### Reiniciar la base de datos local

Esta operación elimina usuarios y datos guardados. Las cuentas de demostración se vuelven a crear al aplicar las migraciones.

```bash
docker compose down
rm backend/db.sqlite3
docker compose up --build
```

### Ejecución local sin Docker

Backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

En Windows, la activación del entorno virtual es:

```bash
.venv\Scripts\activate
```

Frontend, en otra terminal:

```bash
cd frontend
npm install
npm run dev
```

### Variables de entorno

| Variable | Valor por defecto | Uso |
|---|---|---|
| `DJANGO_DEBUG` | `True` | Activa el modo de desarrollo |
| `DJANGO_SECRET_KEY` | Clave de desarrollo | Firma de sesiones y datos sensibles |
| `DJANGO_ALLOWED_HOSTS` | `*` | Hosts permitidos por Django |
| `DJANGO_CORS_ALLOWED_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Orígenes permitidos para el frontend |
| `VITE_API_URL` | `http://localhost:8000` | URL reservada para la futura API del frontend |

Los valores por defecto son exclusivamente para desarrollo.

## Usuarios de prueba

Las siguientes cuentas se crean mediante las migraciones de la aplicación `usuarios`:

| Rol | Usuario | Contraseña | Acceso |
|---|---|---|---|
| Administrador | `admin` | `AdminAula2026!` | Panel administrativo y Django Admin |
| Coordinador Académico | `coordinador` | `Coordinador2026!` | Panel de coordinación |
| Docente | `docente` | `Docente2026!` | Panel del docente |
| Estudiante | `estudiante` | `Estudiante2026!` | Panel del estudiante |

Estas credenciales son solo para desarrollo. En un entorno real deben cambiarse y no deben publicarse.

## Rutas principales

| Ruta | Vista | Acceso |
|---|---|---|
| `/` | Página de inicio | Público |
| `/registro/` | Registro de estudiantes | Público |
| `/login/` | Inicio de sesión | Público |
| `/logout/` | Confirmación y cierre de sesión | Usuarios autenticados |
| `/dashboard/` | Redirección según el rol | Usuarios autenticados |
| `/dashboard/estudiante/` | Panel del estudiante | Rol Estudiante |
| `/dashboard/docente/` | Panel del docente | Rol Docente |
| `/panel/coordinador/` | Panel de coordinación | Rol Coordinador |
| `/panel/administrador/` | Panel administrativo | Rol Administrador |
| `/admin/` | Django Admin | Personal autorizado |

El cierre de sesión se confirma mediante `GET` y se ejecuta mediante `POST`. El superusuario puede acceder a cualquiera de los paneles protegidos.

## Roles y permisos

| Rol | Código | Permisos actuales |
|---|---|---|
| Administrador | `ADMIN` | Acceso al panel administrativo y a Django Admin; superusuario con acceso a todos los paneles |
| Coordinador Académico | `COORD` | Acceso al panel de coordinación |
| Docente | `DOC` | Acceso al panel del docente |
| Estudiante | `EST` | Acceso al panel del estudiante; rol asignado en el registro público |

**Equivalencias con la nomenclatura de la actividad:**

| Término de la actividad | Rol del proyecto |
|---|---|
| Administrador | Administrador |
| Gestor | Coordinador Académico |
| Usuario | Docente o Estudiante, según sus permisos |
| Visitante | Usuario no autenticado |

La protección se implementa con el decorador `rol_requerido`. Si un usuario autenticado intenta abrir un panel que no le corresponde, el sistema muestra un mensaje de error y lo redirige a su propio panel.

## Estado actual y limitaciones

**Implementado:**

- Registro público de estudiantes con validación de correo duplicado.
- Inicio y cierre de sesión.
- Usuario personalizado con rol académico.
- Redirección y protección de paneles por rol.
- Paneles por rol con vistas previas estáticas y accesos reales a Django Admin.
- Métricas reales de usuarios totales, activos y activos por rol en el panel administrativo.
- Administración de usuarios desde Django Admin.
- Interfaz adaptable con tema claro y oscuro.
- Entorno de desarrollo con Docker Compose.

**Pendiente:**

- Períodos académicos.
- Materias y secciones.
- Asignación de docentes a secciones.
- Inscripción de estudiantes a secciones.
- Publicación y administración de anuncios.
- Categorías de anuncios.
- Búsqueda y filtros.
- Notificaciones.
- Integración del frontend Vite con una API de Django.
- Recuperación de contraseña.
- Configuración de producción.

**Limitaciones actuales:**

- Los paneles de estudiante, docente y coordinación combinan vistas previas estáticas con módulos en preparación; el panel administrativo ya muestra métricas reales.
- Las vistas previas usan datos de ejemplo y no representan registros reales de la base.
- Las secciones de ejemplo usan el formato institucional `XX-NN` (FS, M, T, RP, SP y AE); su almacenamiento y validación aún no están implementados.
- No existen todavía modelos de anuncios ni estructura académica.
- La base de datos es SQLite y está pensada para desarrollo.
- El frontend Vite conserva su plantilla inicial y no forma parte de la interfaz visible de AulaBoard.
- La clave secreta y los hosts permitidos usan valores de desarrollo.

## Roadmap

### Fase 1: estructura académica

- Crear el modelo de períodos académicos.
- Registrar materias y secciones por período.
- Asignar docentes responsables a cada sección.
- Permitir que los estudiantes se unan o abandonen secciones.
- Relacionar los paneles con la estructura académica vigente.

### Fase 2: anuncios

- Crear categorías de anuncios.
- Implementar anuncios generales y anuncios por sección.
- Restringir la publicación según el rol y las secciones asignadas.
- Permitir que los estudiantes consulten los anuncios de sus secciones.
- Añadir búsqueda y filtros por categoría, materia, sección, fecha y palabra clave.

### Fase 3: notificaciones y seguimiento

- Notificar la publicación de anuncios en las secciones seguidas.
- Incorporar historial de anuncios activos y vencidos.
- Gestionar la vigencia de los anuncios por período académico.
- Mejorar la accesibilidad y la experiencia en dispositivos móviles.

### Fase 4: administración y crecimiento

- Ampliar las herramientas de administración y supervisión.
- Incorporar reportes de actividad.
- Integrar el frontend Vite mediante una API.
- Preparar la aplicación para un entorno de producción.
- Evaluar el cambio de SQLite a una base de datos relacional de producción.

## Notas de seguridad

Antes de publicar AulaBoard en un entorno real:

- Cambiar `DJANGO_SECRET_KEY` por una clave segura y privada.
- Establecer `DJANGO_DEBUG=False`.
- Restringir `DJANGO_ALLOWED_HOSTS` a los dominios reales.
- Configurar `DJANGO_CORS_ALLOWED_ORIGINS` y `CSRF_TRUSTED_ORIGINS` con los orígenes correctos.
- Cambiar las contraseñas de las cuentas de demostración.
- Utilizar HTTPS.
- Migrar la base de datos a un motor adecuado para producción.
- Revisar los permisos de los usuarios y del panel administrativo.