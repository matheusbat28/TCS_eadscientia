# Imagem base para o Django
FROM python:3.9 as django

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Defina as variáveis de ambiente para a execução do Django
ENV PYTHONUNBUFFERED=1

# Execute as migrações do Django
RUN python manage.py migrate

# Coleta os arquivos estáticos do Django
RUN python manage.py collectstatic --no-input

# Imagem base para o Nginx
FROM nginx:latest

# Copie o arquivo de configuração do Nginx para o contêiner
COPY nginx.conf nginx/nginx.conf

# Copie os arquivos estáticos do Django do contêiner Django para o diretório do Nginx
