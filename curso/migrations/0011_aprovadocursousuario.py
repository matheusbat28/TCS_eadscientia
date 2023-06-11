# Generated by Django 4.1.7 on 2023-06-10 23:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0010_alter_categoria_cursos'),
    ]

    operations = [
        migrations.CreateModel(
            name='AprovadoCursoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_termino', models.DateTimeField(default=datetime.datetime(2023, 6, 25, 20, 39, 53, 273528))),
                ('quantidade_assitido', models.ImageField(upload_to='')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
            ],
            options={
                'verbose_name': 'acesso de curso aluno',
                'verbose_name_plural': 'acessos de cursos alunos',
                'db_table': 'aprovadoCursoUsuario',
            },
        ),
    ]
