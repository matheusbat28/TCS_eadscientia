from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, Capitulo, Video
import json

@login_required
@user_passes_test(lambda u: u.groups.filter(name='autor').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def adicionarCurso(request):
    if request.method == 'POST':
        img = request.FILES.get('inuptFotoCurso')  
        nome = request.POST.get('inputTituloCurso')
        capitulos = []
        
        dadosDicionario = {key: value for key, value in request.POST.items()}
        
        # separar os videos por capitulos
        for key, value in dadosDicionario.items():
            print(key, value)
                

        return JsonResponse({'status': 'successo', 'message': 'Curso adicionado com sucesso!'})
    return render(request, 'adicionarCurso/index.html')