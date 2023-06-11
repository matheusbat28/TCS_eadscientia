from django.urls import path
from . import views

urlpatterns = [
    path('adicionarCurso/', views.adicionarCurso, name='adicionarCurso'),
    path('aprovarCurso/', views.aprovarCurso, name='aprovarCurso'),
    path('buscarCursoAutor/', views.buscarCursoAutor, name='buscarCursoAutor'),
    path('meusCursos/', views.meuCurso, name='meusCursos'),
]