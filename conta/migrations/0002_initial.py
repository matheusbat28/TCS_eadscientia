# Generated by Django 4.1.7 on 2023-04-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cursos',
            field=models.ManyToManyField(blank=True, related_name='cursos', to='curso.curso'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
