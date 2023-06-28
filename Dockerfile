# Usa a imagem base do Python
FROM python:3.8

# Define o diretório de trabalho no contêiner
WORKDIR /code

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . .

# Colete os arquivos estáticos do Django
RUN python manage.py collectstatic --noinput

# Expõe a porta em que o servidor do Django será executado (opcional)
EXPOSE 8000

# Comando para executar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
