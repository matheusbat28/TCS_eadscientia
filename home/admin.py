from django.contrib import admin
from .models import Solicitacao, Curso

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email', 'usuario', 'data_solicitacao', 'criado', 'curso')
    search_fields = ('nome', 'sobrenome', 'cpf', 'email','curso' )
    list_filter = ('data_solicitacao', 'criado', 'curso')
    per_page = 10    
    
admin.site.register(Solicitacao, SolicitacaoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10
    
admin.site.register(Curso, CursoAdmin)