from django.contrib import admin
from .models import Curso, Video, Capitulo

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
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


