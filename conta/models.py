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
    cursos = models.ManyToManyField('home.Curso', related_name='cursos', blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = self.gerar_matricula()
        if not self.username:
            self.username = self.gerar_username()
        super(Usuario, self).save(*args, **kwargs)

    def gerar_matricula(self):
        ultima_matricula = Usuario.objects.all().order_by('matricula').last()
       
        if ultima_matricula:
           matricula = ultima_matricula.matricula
           matricula = int(matricula) + 1
           matricula = str(matricula)
        else:
            matricula = '0'
            
        return matricula.zfill(10)
    
    def gerar_username(self):
        contador = 1
        username = self.get_full_name().strip().lower().replace(' ', '')
        while True:
            if Usuario.objects.filter(username=username).exists():
                username = re.sub(r'\d+', '', username)
                username = username + str(contador)
                contador += 1
            else:
                break
        return username
    
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