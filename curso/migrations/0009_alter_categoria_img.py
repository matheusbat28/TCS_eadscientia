# Generated by Django 4.1.7 on 2023-06-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0008_remove_categoria_img_mini_alter_categoria_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='img',
            field=models.TextField(),
        ),
    ]
