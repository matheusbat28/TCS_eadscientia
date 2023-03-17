from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    per_page = 10
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('infomações Pessoais', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )


admin.site.register(Usuario, UsuarioAdmin)