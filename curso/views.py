from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, Capitulo, Video, AcessoCursoUsuario, Prova, Questao, Alternativa, SolicitarCurso, VideoAssistido
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
    
    if not AcessoCursoUsuario.objects.filter(aluno = request.user, curso = id).exists():
            return redirect('solicitarCurso', id)
          
    curso = get_object_or_404(Curso, id = id)
    statusCurso = AcessoCursoUsuario.objects.get(aluno = request.user, curso = id)
    if request.method == 'POST':
        dataJson = json.loads(request.body)
        id_video = dataJson['id']
        status = dataJson['status']
        
        if status == True:
            video = VideoAssistido.objects.create(
                aluno = request.user,
                curso = curso,
                video = Video.objects.get(id = id_video)
            )
            
            statusCurso.quantidade_assitido.add(video)
        elif status == False:
            video = VideoAssistido.objects.get(
                aluno = request.user,
                video = Video.objects.get(id = id_video),
                curso = curso,
            )
            video.delete()
        
        return JsonResponse({'status': 200, 'message': 'sucesso'})
    else:
        if AcessoCursoUsuario.objects.filter(aluno = request.user, curso = id).exists():
            return render(request, 'assistirCurso/index.html', {'curso': curso, 'statusCurso': statusCurso})
        else:
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
    curso = get_object_or_404(Curso, id= id)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        
        if data == []:
            return JsonResponse({'status': 404, 'message': 'insira pelo menos uma questão'}, safe=False)  
        
        for questao in data:
            pergunta = questao['pergunta']
            opcoes = []
            for altenativa in questao['opcoes']:
                opcoes.append(altenativa['status'])
                
            if not any(opcoes):
                return JsonResponse({'status': 404, 'message': f'insira pelo menos uma altenativa certa na pergunata {pergunta}'}, safe=False)
                
        prova = Prova.objects.create() 
        for questao in data:
            questaodb = Questao.objects.create(
                enuciado = questao['pergunta'].strip()
            )
            for altenativa in questao['opcoes']:   
                alternativadb = Alternativa.objects.create(
                    texto  = altenativa['pergunta'].strip(),
                    selecionada = altenativa['status']
                )
                questaodb.alternativas.add(alternativadb)
             
            prova.questoes.add(questaodb)  
            
            curso.prova = prova
            curso.save()
            
        return JsonResponse({'status': 200, 'message': 'prova criada com suceso'}, safe=False)
    if Curso.objects.filter(id=id, autor = request.user).exists():
        return render(request, 'AdicionarProva/index.html', {'curso': curso, 'pagina': 'Criar avaliação'})
    else:
        messages.error(request, 'Esse curso não pertece a você')
        return redirect('home')
    
@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def deletarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    nome = curso.nome
    
    if curso.prova:
        for questao in curso.prova.questoes.all():
            for alternativa in questao.alternativas.all():
                alternativa.delete()
            questao.delete()
        curso.prova.delete()
    
    for capitulo in curso.capitulos.all():
        for video in capitulo.videos.all():
            video.delete()
        capitulo.delete()
        
    curso.delete()
    
    messages.success(request, f'curso {nome} recusado com sucesso')
    return redirect('aprovarCurso')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def visualizacaoSolicitacaoCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    nome = curso.nome
    
    print(request.POST)
    if request.method == 'POST' and 'btnAprovar' in request.POST:
        curso.aprovado = True
        curso.save()
        messages.success(request, f'o curso {curso.nome} foi aprovado com sucesso ')
        return redirect('aprovarCurso')
                    
    elif request.method == 'POST' and 'btnRecusar' in request.POST:
        for capitulo in curso.capitulos.all():
            for video in capitulo.videos.all():
                video.delete()
            capitulo.delete()
        
        curso.delete()
    
        messages.success(request, f'curso {nome} recusado com sucesso')
        return redirect('aprovarCurso')
    else:
        return render(request, 'visualizacaoSolicitacaoCurso/index.html', {'curso': curso, 'pagina': 'Validar curso'})
  
  
@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')  
def previaCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'previaCurso/index.html', {'curso': curso})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')  
def acessoCurso(request):
    solicitacao = SolicitarCurso.objects.all()
    return render(request, 'acessoCurso/index.html', {'solicitacoes': solicitacao, 'pagina': 'Liberar acesso oa curso'})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def deletarSolicitacaoCurso(request, id):
    solicitacao = get_object_or_404(SolicitarCurso, id=id)
    solicitacao.delete()
    messages.success(request, 'solicitaão recusada com sucesso')
    return redirect('acessoCurso')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def visualizacaoSolicitacaoCursoUsuario(request, id):
    solicitacao = get_object_or_404(SolicitarCurso, id=id)
    
    if 'btnAprovar' in request.POST and request.method == 'POST':
        AcessoCursoUsuario.objects.create(
            aluno = solicitacao.aluno,
            curso = solicitacao.curso
        )
        solicitacao.delete()
        messages.success(request, 'curso liberado com sucesso')
        return redirect('acessoCurso')
    elif 'btnRecusar' in request.POST and request.method == 'POST':
        solicitacao.delete()
        messages.success(request, 'curso recusado com sucesso')
        return redirect('acessoCurso')
    return render(request, 'visualizacaoSolicitacaoCursoUsuario/index.html', {'soilcitacao': solicitacao, 'pagina': 'liberar curso para o usuário'})

@login_required
def fazerAvaliacao(request, id):
    return render(request, 'avaliacao/index.html')