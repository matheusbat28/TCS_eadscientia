# Use uma imagem de Python como base
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o restante do código-fonte para o diretório de trabalho
COPY . .

# Execute o comando para coletar os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Exponha a porta 8000 para o serviço web
EXPOSE 8000

# Defina o comando para iniciar o serviço web
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
