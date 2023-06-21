from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FormSolicitacaoMatricula, FormCriacaoUsuario
from django.contrib import messages
from .models import Solicitacao
from conta.models import Usuario
from curso.models import Categoria, Curso
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.db.models import Q
from curso.models import AcessoCursoUsuario
from curso.forms import FormSolicitarCurso



@login_required
def home(request):
    return render(request, 'home/index.html', {'pesquisa': True, 'categorias': Categoria.objects.all().order_by('?').order_by('nome')[:8], 'cursos_recomendados': Curso.objects.filter(aprovado = True), 'curso_carrocel': Curso.objects.filter(aprovado = True).order_by('?')[:3]})

@login_required
@user_passes_test(lambda u:u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
@user_passes_test(lambda u: u.groups.filter(name='gestão').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def solicitacaoMatricula(request):
    formFormSolicitacaoMatricula = FormSolicitacaoMatricula(request.POST)    
    if request.method == 'POST':
        if formFormSolicitacaoMatricula.is_valid():
            solicitacao = formFormSolicitacaoMatricula.save(request.user)
            if solicitacao is not None:
                messages.success(request, 'Solicitação enviada com sucesso.')
                return redirect('solicitacaoMatricula')
            
        else:
            json = formFormSolicitacaoMatricula.errors.as_json()
            print(json)

            if 'nome' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['nome'][0])
                return redirect('solicitacaoMatricula')
            elif 'sobrenome' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['sobrenome'][0])
                return redirect('solicitacaoMatricula')
            elif 'cpf' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['cpf'][0])
                return redirect('solicitacaoMatricula')
            elif 'email' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['email'][0])
                return redirect('solicitacaoMatricula')
            elif 'motivo' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['motivo'][0])
                return redirect('solicitacaoMatricula')
                
    return render(request, 'socilitarMatricula/index.html', {'formFormSolicitacaoMatricula': formFormSolicitacaoMatricula, 'pagina': 'Solicitação de Matricula'})


     
@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def listarSolicitarMatricula(request):
    termo = request.GET.get('pesquisar')
    query = Solicitacao.objects.all().order_by('sobrenome').order_by('nome')
     
    if termo:
        query = query.filter(
            Q(nome__icontains=termo) | Q(sobrenome__icontains=termo) | Q(email__icontains=termo)
        ).order_by('sobrenome').order_by('nome')
      
    paginator = Paginator(query, 20)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'listarSolicitarMatricula/index.html', {'posts': posts, 'pagina': 'Solicitações de Matricula', 'quantidade': query.count()})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def visualizarSolicitacao(request, id):
    
    solicitacao = get_object_or_404(Solicitacao, id=id)
    grupos = Group.objects.all()
    
    if request.method == 'POST' and 'btnAprovar' in request.POST:
        try:
            grupo = request.POST.get('grupo')
        except Exception:
            pass
        
        if grupo == None:
            grupo = Group.objects.get(name='aluno').id
        if not Group.objects.filter(id=grupo).exists():
            messages.error(request, 'Grupo não existe.')
            return redirect('visualizarSolicitacao', id=id)
        elif Usuario.objects.filter(email=solicitacao.email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('visualizarSolicitacao', id=id)
        elif Usuario.objects.filter(cpf=solicitacao.cpf).exists():
            messages.error(request, 'cpf já cadastrado.')
            return redirect('visualizarSolicitacao', id=id)
        else:
            usuario = Usuario.objects.create(
                first_name=solicitacao.nome,
                last_name=solicitacao.sobrenome,
                email=solicitacao.email,
                cpf=solicitacao.cpf, 
            )
            usuario.groups.add(grupo)
            usuario.save()
            solicitacao.criado = True
            solicitacao.save()
            solicitacao.delete()
            messages.success(request, f'Usuário {usuario.get_full_name()} criado com sucesso.')
            return redirect('listarSolicitarMatricula')
                    
    elif request.method == 'POST' and 'btnRecusar' in request.POST:
        solicitacao.delete()
        messages.success(request, 'Solicitação recusada com sucesso.')
        return redirect('listarSolicitarMatricula')
     
    return render(request, 'visualizacaoSolicitacaoMatricula/index.html', { 'solicitacao': solicitacao, 'pagina': 'visualizar Solicitação', 'grupos': grupos})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def deletarSolicitacao(request, id):
    try:
        solicitacao = Solicitacao.objects.get(id=id)
        solicitacao.delete()
        messages.success(request, 'Solicitação recusada com sucesso.')
        return redirect('listarSolicitarMatricula')
    except Exception:
        messages.error(request, 'Erro ao recusar a solicitação.')
        return redirect('visualizarSolicitacao', id=id)

        
@login_required
@user_passes_test(lambda u: u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def criarUsuario(request):
    formCriacaoUsuario = FormCriacaoUsuario(request.POST)
    if request.method == 'POST':
        if formCriacaoUsuario.is_valid():
            retono = formCriacaoUsuario.save()
            if retono is not None:
                messages.success(request, 'Usuário criado com sucesso.')
                return redirect('criarUsuario')
            else:
                messages.error(request, 'Erro ao criar o usuário.')
                return redirect('criarUsuario')
        else:
            json = formCriacaoUsuario.errors.as_json()
            
            if 'nome' in json:
                messages.error(request, formCriacaoUsuario.errors['nome'][0])
                return redirect('criarUsuario')
            elif 'sobrenome' in json:
                messages.error(request, formCriacaoUsuario.errors['sobrenome'][0])
                return redirect('criarUsuario')
            elif 'cpf' in json:
                messages.error(request, formCriacaoUsuario.errors['cpf'][0])
                return redirect('criarUsuario')
            elif 'email' in json:
                messages.error(request, formCriacaoUsuario.errors['email'][0])
                return redirect('criarUsuario')
            elif 'cursos' in json:
                messages.error(request, formCriacaoUsuario.errors['cursos'][0])
                return redirect('criarUsuario')
            elif 'grupos' in json:
                messages.error(request, formCriacaoUsuario.errors['grupos'][0])
                return redirect('criarUsuario')
            
    return render(request, 'criarUsuario/index.html', {'formCriacaoUsuario': formCriacaoUsuario, 'pagina': 'Criar Usuário'})

@login_required
def curso(request):
    return render(request, 'curso/index.html', {'pagina': 'Cursos a fazer', 'curso_fazer': AcessoCursoUsuario.objects.filter(aluno = request.user)})

@login_required
def categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'categoria/index.html', {'categoria': categoria})

@login_required
def solicitarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    formularioSolicitacaoCurso = FormSolicitarCurso(initial={'aluno': request.user.username, 'curso': curso.nome})
    
    if request.method == 'POST':
        formularioSolicitacaoCurso = FormSolicitarCurso(request.POST)
        print(formularioSolicitacaoCurso.is_valid())
        if formularioSolicitacaoCurso.is_valid():
            retorno = formularioSolicitacaoCurso.save(id)
            
            if retorno:
                messages.success(request, 'Solicitação aprovada')
                return redirect('solicitarCurso', id)
            else:
                messages.error(request, 'erro ao salvar solicitação')
                return redirect('solicitarCurso', id)
        else: 
            json = formularioSolicitacaoCurso.errors.as_json()
            print(json)
            if 'aluno' in json:
                messages.error(request, formularioSolicitacaoCurso.errors['aluno'][0])
                return redirect('solicitarCurso', id)
            elif 'curso' in json:
                messages.error(request, formularioSolicitacaoCurso.errors['curso'][0])
                return redirect('solicitarCurso', id)   
            elif 'motivo' in json:
                messages.error(request, formularioSolicitacaoCurso.errors['motivo'][0])
                return redirect('solicitarCurso', id)
    return render(request, 'solicitarCurso/index.html', {'curso': curso, 'formularioSolicitacaoCurso': formularioSolicitacaoCurso})