# Generated by Django 4.1.7 on 2023-06-19 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0013_alter_acessocursousuario_data_termino_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acessocursousuario',
            name='data_termino',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 21, 24, 38, 909918)),
        ),
    ]
