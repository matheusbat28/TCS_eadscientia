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
        print(request.POST)
        # nome_curso = request.POST.get('nome-curso').strip()
        json_capitulo = json.loads(request.POST.get('capitulos'))
        # foto_curso = request.FILES.get('inuptFotoCurso')
        
        # if not nome_curso:
        #     return JsonResponse({'status': 'erro', 'message': 'Insira um nome para o curso'})
        # elif not foto_curso:
        #     return JsonResponse({'status': 'erro', 'message': 'Insira um foto para o curso'})
        
        # for capitulo in json_capitulo:
        #     for video in capitulo['videos']:
        #         for chave, valor in video.items():
        #             if chave == 'url-video':
        #                 if not validar_youtube_url(valor):
        #                     return JsonResponse({'status': 'erro', 'message': f'A url {valor} não é valida'})
                            
        # curso = Curso.objects.create(
        #     nome = nome_curso,
        #     img = foto_curso,
        #     autor = request.user
        # )
        
        # print(curso)
        
        for capitulo in json_capitulo:
            for video in capitulo['videos']:
                print(video)
                

        return JsonResponse({'status': 'successo', 'message': 'Curso adicionado com sucesso!'})
    return render(request, 'adicionarCurso/index.html')