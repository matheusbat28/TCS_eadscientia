from django.urls import path
from . import views

urlpatterns = [
    path('adicionarCurso/', views.adicionarCurso, name='adicionarCurso'),
    path('aprovarCurso/', views.aprovarCurso, name='aprovarCurso'),
    path('acessoCurso/', views.acessoCurso, name='acessoCurso'),
    path('meusCursos/', views.meuCurso, name='meusCursos'),
    path('assistirVideo/<int:id>', views.assistirVideo, name='assistirVideo'),
    path('previaCurso/<int:id>', views.previaCurso, name='previaCurso'),
    path('todoCurso/', views.todoCurso, name='todoCurso'),
    path('adicionarProva/<int:id>', views.adicionarProva, name='adicionarProva'),
    path('deletarCurso/<int:id>', views.deletarCurso, name='deletarCurso'),
    path('deletarSolicitacaoCurso/<int:id>', views.deletarSolicitacaoCurso, name='deletarSolicitacaoCurso'),
    path('visualizacaoSolicitacaoCurso/<int:id>', views.visualizacaoSolicitacaoCurso, name='visualizacaoSolicitacaoCurso'),
]