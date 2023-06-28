from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, Capitulo, Video, AcessoCursoUsuario
from conta.models import Usuario
from .apis import validar_youtube_url, tempo_video_youtube, obter_id_video_youtube
import json
from django.core import serializers

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
                        return JsonResponse({'status': 404, 'message': f'a url {video["url"]} do video {video["nome"]} não é uma valida no youtube'}, status=200)
            valido = True
            
        if  capitulos != [] and valido:
            curso = Curso.objects.create(
                nome = nome_curso,
                autor = request.user,
                img = foto_curso
            )   
            
            try:
                for capitulo in capitulos: 
                    capitulo_db = Capitulo.objects.create(
                        titulo = capitulo['nome-capitulo'],
                        autor = request.user,
                    )
                    for video in capitulo['videos']:
                        video_db = Video.objects.create(
                            titulo = video["nome"],
                            video = obter_id_video_youtube(video["url"]),
                            autor = request.user,
                            duracao = tempo_video_youtube(video["url"])
                        )
                        capitulo_db.videos.add(video_db)
                    curso.capitulos.add(capitulo_db)
            except Exception:
                return JsonResponse({'status': 404, 'message': 'erro ao gerar o curso'}, status=200)
                    
            
        return JsonResponse({'status': 200, 'message': 'Curso adicionado com sucesso!'}, status=200)
    return render(request, 'adicionarCurso/index.html', {'pagina': 'Criar curso'})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def aprovarCurso(request):
        cursos = Curso.objects.filter(aprovado=False)
        return render(request, 'aprovarCurso/index.html', {'pagina': 'Aprovar curso', 'cursos': cursos})
    
@login_required
@user_passes_test(lambda u: u.groups.filter(name='autor').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def meuCurso(request):
    curso = Curso.objects.filter(autor = request.user)
    return render(request, 'meuCurso/index.html', {'curso': curso})

@login_required
def assistirVideo(request, id):
    if AcessoCursoUsuario.objects.filter(aluno = request.user, curso = id).exists():
        return render(request, 'assistirCurso/index.html', {'curso': Curso.objects.get(id = id), 'statusCurso': AcessoCursoUsuario.objects.get(aluno = request.user, curso = id)})
    else:
        curso = Curso.objects.get(id = id)
        messages.error(request, f'Não tem acesso ao curso {curso.nome}')
        return redirect('solicitarCurso', id)
    
@login_required
def todoCurso(request):
    cursos = Curso.objects.filter(aprovado = True)
    cursos_serialized = serializers.serialize('json', cursos)
    return JsonResponse({'status': 200, 'curso': cursos_serialized}, safe=False)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='autor').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def adicionarProva(request, id):
    
    if request.method == 'POST':
        json = request.POST
        
        print(json)        
        
        return JsonResponse({'status': 200, 'mensagem': 'entrou'}, safe=False)
    if Curso.objects.filter(id=id, autor = request.user).exists():
        curso = Curso.objects.get(id = id)
        return render(request, 'AdicionarProva/index.html', {'curso': curso, 'pagina': 'Criar avaliação'})
    else:
        messages.error(request, 'Esse curso não pertece a você')
        return redirect('home')