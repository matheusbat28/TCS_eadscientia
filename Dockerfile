# Use uma imagem base Python
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o código do projeto para o contêiner
COPY . .

# Defina o comando de execução padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
