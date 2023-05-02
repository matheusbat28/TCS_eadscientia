from django.contrib import admin
from .models import Curso, Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    search_fields = ('titulo', 'autor')
    list_filter = ('titulo', 'autor')
    per_page = 10
    
admin.site.register(Video, VideoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10
    
admin.site.register(Curso, CursoAdmin)


