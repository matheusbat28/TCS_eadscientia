from django.contrib import admin
from .models import Curso, Video, Capitulo, Categoria, AcessoCursoUsuario, SolicitarCurso, Prova, Questao, Alternativa, VideoAssistido, Historico


class ProvaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'duracao')
    search_fields = ('data_criacao', )
    list_filter = ('data_criacao', 'duracao')
    per_page = 10
    
admin.site.register(Prova, ProvaAdmin)

class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('enuciado',)
    search_fields = ('enuciado', )
    list_filter = ('enuciado',)
    per_page = 10
    
admin.site.register(Questao, QuestaoAdmin)

class AlternativaAdmin(admin.ModelAdmin):
    list_display = ('texto',)
    search_fields = ('texto',)
    list_filter = ('texto',)
    per_page = 10
    
admin.site.register(Alternativa, AlternativaAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'duracao', 'video')
    search_fields = ('titulo',)
    list_filter = ('titulo',)
    per_page = 10
    
admin.site.register(Video, VideoAdmin)


class CapituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('titulo',)
    list_filter = ('titulo',)
    per_page = 10
    
admin.site.register(Capitulo, CapituloAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'aprovado')
    search_fields = ('nome',)
    list_filter = ('nome', 'aprovado')
    per_page = 10
    
admin.site.register(Curso, CursoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10


admin.site.register(Categoria, CategoriaAdmin)

class AcessoCursoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_termino', 'status_prova')
    search_fields = ('aluno', 'curso')
    list_filter = ('aluno', 'curso', 'data_termino')
    per_page = 10


admin.site.register(AcessoCursoUsuario, AcessoCursoUsuarioAdmin)


class SolicitarCursoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_criacao')
    search_fields = ('aluno', 'curso')
    list_filter = ('aluno', 'curso', 'data_criacao')
    per_page = 10
    
admin.site.register(SolicitarCurso, SolicitarCursoAdmin)

class VideoAssistidoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_criacao')
    search_fields = ('aluno', 'curso')
    list_filter = ('aluno', 'curso', 'data_criacao')
    per_page = 10

admin.site.register(VideoAssistido, VideoAssistidoAdmin)

class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_criacao', 'status_prova')
    search_fields = ('aluno', 'curso', 'status_prova')
    list_filter = ('aluno', 'curso', 'status_prova', 'data_criacao')
    per_page = 10

admin.site.register(Historico, HistoricoAdmin)