FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY templates /app/templates
COPY staticfiles /app/staticfiles

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
