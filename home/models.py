from django.db import models
from cpf_field.models import CPFField
from django.utils.timezone import now

class Solicitacao(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = CPFField('CPF', unique=True)
    email = models.EmailField()
    usuario = models.ForeignKey('conta.Usuario', on_delete=models.DO_NOTHING)
    data_solicitacao = models.DateTimeField(default=now)

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'solicitacao'
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'