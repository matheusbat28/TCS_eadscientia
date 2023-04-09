from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('solicitacaomMatricula/', views.solicitacaomMatricula, name='solicitacaomMatricula'),
    path('listarSolicitarMatricula/', views.listarSolicitarMatricula, name='listarSolicitarMatricula'),
    path('visualizarSolicitacao/<int:id>', views.visualizarSolicitacao, name='visualizarSolicitacao'),
    path('criarSolicitacao/<int:id>', views.criarSolicitacao, name='criarSolicitacao'),
    path('deletarSolicitacao/<int:id>', views.deletarSolicitacao, name='deletarSolicitacao'),
]