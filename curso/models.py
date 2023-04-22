from django.db import models
from django.utils import timezone



class Curso(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ManyToManyField('conta.Usuario', related_name='autor')
    data_criacao = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
