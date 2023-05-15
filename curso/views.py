from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Curso, Capitulo, Video
import json

@login_required
def adicionarCurso(request):
    if request.method == 'POST':
        validator = URLValidator()
        json_data = json.loads(request.body)
        nome = json_data['nomeCurso']
        capitulos = json_data['capitulos']
        valido = False
        if capitulos == []:
            return JsonResponse({'message': 'Adicione pelo menos um capítulo!'})
        else:
            for capitulo in capitulos:
                for video in capitulo['video']:  
                    try:
                        validator(video['urlVideo'])
                    except ValidationError:
                        return JsonResponse({'message': f'URL inválida: {video["urlVideo"]} do capítulo {capitulo["nomeCapitulo"]} no vídeo {video["nomeVideo"]}'})
            valido = True
        if valido:
            curso = Curso.objects.create(nome=nome, autor=request.user)
            for capitulo in capitulos:
                cap = Capitulo.objects.create(titulo=capitulo['nomeCapitulo'])
                for video in capitulo['video']:
                    vid = Video.objects.create(titulo=video['nomeVideo'], video=video['urlVideo'])
                    cap.videos.add(vid)
                    cap.save()
                curso.capitulos.add(cap)
                curso.save()
                     
       
                   
        return JsonResponse({'status': 'successo', 'message': 'Curso adicionado com sucesso!'})
    return render(request, 'adicionarCurso/index.html')