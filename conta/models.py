from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField
from django.utils.timezone import now

class Usuario(AbstractUser):

    matricula = models.CharField(max_length=10, unique=True)
    cpf = CPFField('CPF', unique=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Token(models.Model):
    token = models.CharField(max_length=255, unique=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    validou = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=now)

    def __str__(self):
        return self.token
    
    class Meta:
        db_table = 'token'
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'