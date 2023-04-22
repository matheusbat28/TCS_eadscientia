from django.contrib import admin
from .models import Solicitacao

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email', 'usuario', 'data_solicitacao', 'criado')
    search_fields = ('nome', 'sobrenome', 'cpf', 'email' )
    list_filter = ('data_solicitacao', 'criado')
    per_page = 10    
    
admin.site.register(Solicitacao, SolicitacaoAdmin)
