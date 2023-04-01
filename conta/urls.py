from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('verificar_codigo/<int:id>/', views.verificar_codigo, name='verificar_codigo'),
    path('recuperar_senha/<int:id>/', views.recuperar_senha, name='recuperar_senha'),
    path('remandar_codigo/<int:id>/', views.remandar_codigo, name='remandar_codigo')
]