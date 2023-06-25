# Imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Define as variáveis de ambiente para a execução do Django
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV PYTHONUNBUFFERED=1

# Cria o ambiente virtual
RUN python -m venv venv

# Ativa o ambiente virtual
RUN /bin/bash -c "source venv/bin/activate"

# Instala as dependências do projeto
RUN pip install --no-cache-dir --use-feature=fast-deps -r requirements.txt

# Executa as migrações do Django
RUN python manage.py migrate

# Coleta os arquivos estáticos do Django
RUN python manage.py collectstatic --no-input

# Expõe a porta do aplicativo (ajuste se necessário)
EXPOSE 8000

# Comando para iniciar o aplicativo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
