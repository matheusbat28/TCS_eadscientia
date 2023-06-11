from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    video = models.URLField(max_length=200)
    data_criacao = models.DateTimeField(default=timezone.now)
    duracao = models.TimeField(blank=True, null=True)
    autor = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)
    
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
    autor = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)
      
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
    img = models.ImageField(upload_to='curso/%Y/%m/%d', default='curso/img/curso.png')
    aprovado = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    img = models.TextField()
    cursos = models.ManyToManyField('curso.Curso', blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categoria'

 
class AcessoCursoUsuario(models.Model):
    aluno = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)   
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE)
    data_termino = models.DateTimeField(default=datetime.now() + timedelta(days=15))
    quantidade_assitido = models.IntegerField()
    status_prova = models.BooleanField(default=False)
    
    def __str__(self):
        return self.aluno.get_full_name()
    
    class Meta:
        db_table = 'acessoCursoUsuario'
        verbose_name = 'acesso de curso aluno'
        verbose_name_plural = 'acessos de cursos alunos'
        