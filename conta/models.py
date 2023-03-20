from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField

class Usuario(AbstractUser):

    matricula = models.CharField(max_length=10, unique=True)
    cpf = CPFField('CPF', unique=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
