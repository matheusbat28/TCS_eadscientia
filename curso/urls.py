from django.urls import path
from . import views

urlpatterns = [
    path('adicionarCurso/', views.adicionarCurso, name='adicionarCurso'),
    path('aprovarCurso/', views.aprovarCurso, name='aprovarCurso'),
    path('meusCursos/', views.meuCurso, name='meusCursos'),
    path('assistirVideo/<int:id>', views.assistirVideo, name='assistirVideo'),
    path('todoCurso/', views.todoCurso, name='todoCurso'),
    path('adicionarProva/<int:id>', views.adicionarProva, name='adicionarProva'),
    path('deletarCurso/<int:id>', views.deletarCurso, name='deletarCurso'),
]