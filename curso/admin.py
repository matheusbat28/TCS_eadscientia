from django.contrib import admin
from .models import Curso, Categoria, ModuloCurso, VideoCurso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10
    
admin.site.register(Curso, CursoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10
    
admin.site.register(Categoria, CategoriaAdmin)
    
class VideoCursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10
    
admin.site.register(VideoCurso, VideoCursoAdmin)
    
class ModuloCursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    per_page = 10
    
admin.site.register(ModuloCurso, ModuloCursoAdmin)

