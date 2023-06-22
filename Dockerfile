# Estágio de compilação
FROM python:3.9 as builder

# Configurações de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho
WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do aplicativo
COPY . .

# Executar migrações e coletar arquivos estáticos (se necessário)
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

# Estágio de produção
FROM nginx:latest

# Copiar o arquivo de configuração do Nginx
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Copiar arquivos estáticos do estágio de compilação
COPY --from=builder /app/staticfiles /staticfiles

# Expôr a porta 80 para acesso externo
EXPOSE 80
