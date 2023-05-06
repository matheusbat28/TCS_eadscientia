from django.urls import path
from . import views

urlpatterns = [
    path('adicionarCurso/', views.adicionarCurso, name='adicionarCurso'),
]