from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('solicitacaoMatricula/', views.solicitacaoMatricula, name='solicitacaoMatricula'),
    path('listarSolicitarMatricula/', views.listarSolicitarMatricula, name='listarSolicitarMatricula'),
    path('visualizarSolicitacao/<int:id>', views.visualizarSolicitacao, name='visualizarSolicitacao'),
    path('deletarSolicitacao/<int:id>', views.deletarSolicitacao, name='deletarSolicitacao'),
    path('criarUsuario/', views.criarUsuario, name='criarUsuario'),
    path('curso/', views.curso, name='curso'),
    path('categoria/<int:id>/', views.categoria, name='categoria'),
    path('solicitarCurso/<int:id>/', views.solicitarCurso, name='solicitarCurso'),
    
]