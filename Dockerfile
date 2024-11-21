FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y gcc libpq-dev

# Configurar el directorio de trabajo
WORKDIR /usr/src/app

# Copiar dependencias del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando de inicio
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]