# Imagen base de Python
FROM python:3.12-slim

# Evita generar archivos .pyc y muestra los logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala dependencias antes de copiar el codigo (mejor cache)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Puerto del servidor Django
EXPOSE 8000

# Comando por defecto; docker-compose lo reemplaza para migrar antes
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
