# Usa a imagem base do Python
FROM python:3.8

# Define o diretório de trabalho no contêiner
WORKDIR /code

# Copia o código do projeto para o contêiner
COPY . .

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Colete os arquivos estáticos do Django
RUN python manage.py collectstatic --noinput

# Exponha a porta 8000 para o Gunicorn
EXPOSE 8000

# Comando para iniciar o Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
