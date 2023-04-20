from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    curso = models.ManyToManyField('curso.Curso', related_name='curso')
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
class VideoCurso(models.Model):
    nome = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%Y/%m/%d')
    modulo = models.ForeignKey('curso.ModuloCurso', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'video_curso'
        verbose_name = 'Video Curso'
        verbose_name_plural = 'Videos Curso'
        
class ModuloCurso(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'modulo_curso'
        verbose_name = 'Modulo Curso'
        verbose_name_plural = 'Modulos Curso'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ManyToManyField('conta.Usuario', related_name='autor')
    data_criacao = models.DateTimeField(default=timezone.now)
    modulo = models.ManyToManyField('curso.ModuloCurso', related_name='modulo')
    descricao = models.TextField()
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
