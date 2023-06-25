# Estágio de construção
FROM python:3.9 AS builder

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Executa as migrações do Django
RUN python manage.py migrate

# Coleta os arquivos estáticos do Django
RUN python manage.py collectstatic --no-input

# Estágio de produção
FROM nginx:latest

# Copia os arquivos estáticos e de configuração do Nginx do estágio de construção
COPY --from=builder /app/staticfiles /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta 80 para o Nginx
EXPOSE 80

# Inicia o servidor Nginx
CMD ["nginx", "-g", "daemon off;"]
