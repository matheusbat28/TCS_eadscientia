from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField
from django.utils.timezone import now
import re
class Usuario(AbstractUser):

    email = models.EmailField(unique=True, verbose_name='E-mail', blank=True, null=True)
    matricula = models.CharField(max_length=10, unique=True)
    cpf = CPFField('CPF', unique=True)
    imagem_perfil = models.ImageField(upload_to='perfil_img/%Y/%m/%d', blank=True, null=True)
    cursos_aprovados = models.ManyToManyField('curso.Curso', blank=True)

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Token(models.Model):
    token = models.CharField(max_length=255, unique=True, blank=True, null=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    validou = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=now)

    def __str__(self):
        return self.token
    
    class Meta:
        db_table = 'token'
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        