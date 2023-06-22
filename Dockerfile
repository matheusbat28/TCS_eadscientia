# Imagem base
FROM python:3.9

# Configurações de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho
WORKDIR /app

# Instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do aplicativo
COPY . .

# Executar migrações
RUN python manage.py migrate

# Iniciar o aplicativo
CMD python manage.py runserver 0.0.0.0:8000
