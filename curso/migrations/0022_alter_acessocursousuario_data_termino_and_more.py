# Generated by Django 4.1.7 on 2023-06-30 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0021_alter_acessocursousuario_data_termino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessocursousuario',
            name='data_termino',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 15, 44, 13, 910178)),
        ),
        migrations.AlterField(
            model_name='alternativa',
            name='texto',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='solicitarcurso',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 30, 15, 44, 13, 911208)),
        ),
    ]
