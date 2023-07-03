from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class Alternativa(models.Model):
    texto = models.TextField()
    selecionada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.texto
    
    class Meta:
        db_table = 'alternativa'
        verbose_name = 'alternativa'
        verbose_name_plural = 'alternativas'

class Questao(models.Model):
    enuciado = models.CharField(max_length=250)
    alternativas = models.ManyToManyField('curso.Alternativa')
    
    def __str__(self):
        return self.enuciado
    
    class Meta:
        db_table = 'questao'
        verbose_name = 'questão'
        verbose_name_plural = 'questões'

class Prova(models.Model):
    questoes = models.ManyToManyField('curso.Questao')
    data_criacao = models.DateTimeField(default=timezone.now)
    duracao = models.DurationField(default=timedelta(hours=1), blank=True, null=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'prova'
        verbose_name = 'prova'
        verbose_name_plural = 'provas'

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    video = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)
    duracao = models.TimeField(blank=True, null=True)
    autor = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} {self.video}'
    
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
        return f'{self.id} {self.titulo}'
    
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
    prova = models.OneToOneField('curso.Prova', on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.TextField()
    
    
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
        verbose_name_plural = 'categorias'


class VideoAssistido(models.Model):
    aluno = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)   
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE)
    video = models.ForeignKey('curso.Video', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.aluno.get_full_name()
    
    class Meta:
        db_table = 'video assistido'
        verbose_name = 'video assistido'
        verbose_name_plural = 'videos assistido'
 
class AcessoCursoUsuario(models.Model):
    aluno = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)   
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE)
    data_termino = models.DateTimeField(default=datetime.now() + timedelta(days=15))
    quantidade_assitido = models.ManyToManyField('curso.VideoAssistido', blank=True)
    status_prova = models.BooleanField(default=False)
    
    def __str__(self):
        return self.aluno.get_full_name()
    
    class Meta:
        db_table = 'acessoCursoUsuario'
        verbose_name = 'acesso de curso aluno'
        verbose_name_plural = 'acessos de cursos alunos'
        
class SolicitarCurso(models.Model):
    aluno = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE)   
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=datetime.now())
    motivo = models.TextField()
    
    class Meta:
        db_table = 'solicitarCurso'
        verbose_name = 'solicitar o curso'
        verbose_name_plural = 'solicitações os cursos'
        
class Historico(models.Model):
    aluno = models.ForeignKey('conta.Usuario', on_delete=models.CASCADE) 
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=datetime.now())  
    status_prova = models.BooleanField()
    procentagem = models.IntegerField() 
    
    def __str__(self):
        return self.aluno.get_full_name()
    
    class Meta:
        db_table = 'historico'
        verbose_name = 'historico'
        verbose_name_plural = 'historicos' 