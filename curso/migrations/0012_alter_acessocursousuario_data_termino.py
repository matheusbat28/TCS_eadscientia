# Generated by Django 4.1.7 on 2023-06-11 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0011_video_duracao_acessocursousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessocursousuario',
            name='data_termino',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 16, 58, 0, 441098)),
        ),
    ]
