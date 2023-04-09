from django.db import models
from cpf_field.models import CPFField
from django.utils.timezone import now

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
class Solicitacao(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = CPFField('CPF', unique=True)
    email = models.EmailField()
    curso = models.ForeignKey('home.Curso', on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey('conta.Usuario', on_delete=models.DO_NOTHING)
    data_solicitacao = models.DateTimeField(default=now)
    criado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    

    class Meta:
        db_table = 'solicitacao'
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
        
