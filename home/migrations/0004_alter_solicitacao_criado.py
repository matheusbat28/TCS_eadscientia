# Generated by Django 4.1.7 on 2023-04-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_solicitacao_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='criado',
            field=models.BooleanField(default=False, verbose_name='Validado'),
        ),
    ]
