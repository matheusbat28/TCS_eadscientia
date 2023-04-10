from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Token


class UsuarioAdmin(UserAdmin):
    list_display = ('username','matricula', 'cpf', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'matricula', 'cpf', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    per_page = 10
    fieldsets = (
        (None, {
            'fields': ('username', 'matricula', 'password', 'first_name', 'last_name', 'email', 'cpf', 'imagem_perfil', 'cursos')
        }),
        ('Permissôes', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )


admin.site.register(Usuario, UsuarioAdmin)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'usuario', 'validou', 'data_criacao')
    search_fields = ('token', 'usuario')
    list_filter = ('validou',)
    per_page = 10
    
    
admin.site.register(Token, TokenAdmin)