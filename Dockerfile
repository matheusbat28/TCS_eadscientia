# Use a imagem base Python
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie todo o código fonte do projeto para o diretório de trabalho
COPY . .

# Defina as variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Execute o comando para migrar o banco de dados
RUN python manage.py migrate

# Exponha a porta em que o servidor Django estará rodando
EXPOSE 8000

# Inicie o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
