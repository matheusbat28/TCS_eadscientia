# Generated by Django 4.1.7 on 2023-06-21 02:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0014_curso_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessocursousuario',
            name='data_termino',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 23, 47, 54, 33599)),
        ),
        migrations.CreateModel(
            name='SolicitarCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=datetime.datetime(2023, 6, 20, 23, 47, 54, 33599))),
                ('motivo', models.TextField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
            ],
            options={
                'verbose_name': 'solicitar o curso',
                'verbose_name_plural': 'solicitações os cursos',
                'db_table': 'solicitarCurso',
            },
        ),
    ]
