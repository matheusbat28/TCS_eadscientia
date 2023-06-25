# Define a imagem base
FROM python:3.9

# Configuração do ambiente
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho dentro do contêiner
WORKDIR /code

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt /code/

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o código fonte para o contêiner
COPY . /code/

# Executa as migrações do Django
RUN python manage.py migrate

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Comando para executar o servidor Django
CMD python manage.py runserver 0.0.0.0:8000
