FROM python:latest

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

COPY . .

RUN python manage.py collectstatic --noinput

# Adicione as linhas abaixo para instalar o pacote OpenSSL e seus certificados
RUN apt-get update && apt-get install -y openssl ca-certificates

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
