# Imagem base
FROM python:3.8

# Define o diretório de trabalho
WORKDIR .

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . .

# Expõe a porta do servidor Django
EXPOSE 8000

# Comando para executar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
