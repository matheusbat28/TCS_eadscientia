from django.urls import path
from . import views

urlpatterns = [
    path('adicioanarVideo/', views.adicionarVideo, name='adicionarVideo'),
]