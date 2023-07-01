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

# Instale o Certbot
RUN apt-get update && apt-get install -y certbot

# Copie o script de inicialização do Certbot
COPY init_certbot.sh /code/init_certbot.sh

# Defina permissões de execução para o script
RUN chmod +x /code/setup-ssl.sh

# Execute o script de inicialização do Certbot antes de iniciar o serviço web
CMD ["/code/init_certbot.sh"]
