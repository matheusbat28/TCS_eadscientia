FROM python:latest

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
