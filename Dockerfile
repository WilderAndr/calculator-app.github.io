# Usamos una imagen base de Python
FROM python:3.8-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos necesarios
COPY . /app

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Exponemos el puerto 5000 (Flask)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
