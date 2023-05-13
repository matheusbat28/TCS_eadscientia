from django.db import models
from django.utils import timezone

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%Y/%m/%d')
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'video'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        
class Capitulo(models.Model):
    titulo = models.CharField(max_length=100)
    videos = models.ManyToManyField('curso.Video')
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'capitulo'
        verbose_name = 'Capitulo'
        verbose_name_plural = 'Capitulos'
        

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    capitulos = models.ManyToManyField('curso.Capitulo')
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
