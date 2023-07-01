FROM python:latest

# Instalar dependências do sistema operacional
RUN apt-get update && apt-get install -y nginx

# Configurar Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Configurar certificado SSL
COPY cert.pem /etc/nginx/cert.pem
COPY privkey.pem /etc/nginx/privkey.pem
COPY chain.pem /etc/nginx/chain.pem

# Copiar o código do aplicativo
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Configurar Nginx para encaminhar solicitações para o aplicativo Django
RUN python manage.py collectstatic --noinput

# Expor a porta 80 para HTTP e 443 para HTTPS
EXPOSE 80
EXPOSE 443

# Iniciar o servidor Nginx e o aplicativo Django com Gunicorn
CMD service nginx start && gunicorn config.wsgi:application --bind 0.0.0.0:8000
