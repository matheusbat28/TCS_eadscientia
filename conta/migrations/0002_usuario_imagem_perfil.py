# Generated by Django 4.1.7 on 2023-04-03 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem_perfil',
            field=models.ImageField(default=1, upload_to='perfil_img/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
