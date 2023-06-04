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
        foto_curso = request.FILES.get('inuptFotoCurso')
        capitulos = json.loads(request.POST.get('capitulos'))
        valido = False
        
        if foto_curso is None:
            return JsonResponse({'status': 404, 'message': 'Insira uma foto para a capa do curso'})
        elif nome_curso is None:
            return JsonResponse({'status': 404, 'message': 'Insira uma nome para curso'})
        elif capitulos == []: 
            return JsonResponse({'status': 404, 'message': 'Insira uma capitulo para o curso'})
        elif capitulos != []:
            for capitulo in capitulos:
                for video in capitulo['videos']:
                    if not validar_youtube_url(video['url']):
                        return JsonResponse({'status': 404, 'message': f'a url {video["url"]} do video {video["nome"]} não é uma valida no youtube'})
            valido = True
        if  capitulos != [] and valido:
            curso = Curso.objects.create(
                nome = nome_curso,
                autor = request.user,
                img = foto_curso
            )   
            
            for capitulo in capitulos: 
                capitulo_db = Capitulo.objects.create(
                   titulo = capitulo['nome-capitulo'],
                   autor = request.user,
                )
                for video in capitulo['videos']:
                    video_db = Video.objects.create(
                        titulo = video["nome"],
                        video = video["url"],
                        autor = request.user,
                    )
                    capitulo_db.videos.add(video_db)
                curso.capitulos.add(capitulo_db)
                
            
        return JsonResponse({'status': 200, 'message': 'Curso adicionado com sucesso!'})
    return render(request, 'adicionarCurso/index.html')