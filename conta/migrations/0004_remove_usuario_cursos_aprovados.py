# Generated by Django 4.1.7 on 2023-06-11 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0003_remove_usuario_cursos_usuario_cursos_aprovados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cursos_aprovados',
        ),
    ]
