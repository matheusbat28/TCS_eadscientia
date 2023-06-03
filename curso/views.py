from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, Capitulo, Video
from .apis import validar_youtube_url
import json

@login_required
@user_passes_test(lambda u: u.groups.filter(name='autor').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def adicionarCurso(request):
    if request.method == 'POST':
        nome_curso = request.POST.get('nome-curso')
        foto_curso = request.POST.get('inuptFotoCurso')
        capitulos = json.loads(request.POST.get('capitulos'))
        
        print(request.POST)
        # for capitulo in capitulos:
        #     print(capitulo)

        return JsonResponse({'status': 'successo', 'message': 'Curso adicionado com sucesso!'})
    return render(request, 'adicionarCurso/index.html')