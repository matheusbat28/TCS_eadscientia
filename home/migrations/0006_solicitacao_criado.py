# Generated by Django 4.1.7 on 2023-04-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_solicitacao_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='criado',
            field=models.BooleanField(default=False),
        ),
    ]
