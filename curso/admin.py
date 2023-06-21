from django.contrib import admin
from .models import Curso, Video, Capitulo, Categoria, AcessoCursoUsuario, SolicitarCurso

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'duracao', 'video')
    search_fields = ('titulo',)
    list_filter = ('titulo',)
    per_page = 10
    
admin.site.register(Video, VideoAdmin)

class CapituloAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
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
    list_display = ('aluno', 'curso', 'data_termino', 'quantidade_assitido', 'status_prova')
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
