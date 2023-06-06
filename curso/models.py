from django.db import models
from django.utils import timezone

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    video = models.URLField(max_length=200)
    data_criacao = models.DateTimeField(default=timezone.now)
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
    img = models.FileField(upload_to='categoria/%Y/%m/%d', default='curso/img/curso.png')
    cursos = models.ManyToManyField('curso.Curso')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categoria'