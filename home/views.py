from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FormSolicitacaoMatricula, FormCriacaoUsuario
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Solicitacao
from conta.models import Usuario
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
import random
import string


@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
@user_passes_test(lambda u:u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
@user_passes_test(lambda u: u.groups.filter(name='gestão').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def solicitacaoMatricula(request):
    formFormSolicitacaoMatricula = FormSolicitacaoMatricula(request.POST)    
    if request.method == 'POST':
        if formFormSolicitacaoMatricula.is_valid():
            solicitacao = formFormSolicitacaoMatricula.save(request.user)
            if solicitacao is not None:
                mandar_email(email=settings.EMAIL_RH, solicitacao=solicitacao, tipo='solicitacao', usuario=request.user)
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
    solicitacoes = Solicitacao.objects.filter(criado=False).order_by('sobrenome').order_by('nome')
    paginator = Paginator(solicitacoes, 10)
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'listarSolicitarMatricula/index.html', {'posts': posts, 'pagina': 'Solicitações de Matricula'})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def visualizarSolicitacao(request, id):
    
    
    solicitacao = Solicitacao.objects.get(id=id)
    grupos = Group.objects.all()
    return render(request, 'visualizacaoSolicitacaoMatricula/index.html', { 'solicitacao': solicitacao, 'pagina': 'visualizar Solicitação', 'grupos': grupos})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='recuso humano').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def deletarSolicitacao(request, id):
    try:
            solicitacao = Solicitacao.objects.get(id=id)
            solicitacao.delete()
            mandar_email(email=solicitacao.email, solicitacao=solicitacao, tipo='recusacao')
            messages.success(request, 'Solicitação recusada com sucesso.')
            return redirect('listarSolicitarMatricula')
    except Exception:
        messages.error(request, 'Erro ao recusar a solicitação.')
        return redirect('visualizarSolicitacao', id=id)

def gararSenhaAleatoria():
    letras = string.ascii_letters
    numeros = string.digits
    caracteres = letras + numeros
    senha = ''.join(random.choice(caracteres) for i in range(8))
    return senha

def mandar_email(email, solicitacao=None, tipo=None, usuario=None, senha=None, usuarioADM=None):
    if tipo == 'solicitacao':
        html_contexto = render_to_string('email/solicitacaoMatricula.html', {'solicitacao': solicitacao, 'usuario': usuario})
        texto_contexto = strip_tags(html_contexto)
        
        email = EmailMultiAlternatives(
            'Solicitação de Matricula',
            texto_contexto,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.attach_alternative(html_contexto, "text/html")
        email.send()
        
@login_required
@user_passes_test(lambda u: u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def criarUsuario(request):
    formCriacaoUsuario = FormCriacaoUsuario(request.POST)
    if request.method == 'POST':
        if formCriacaoUsuario.is_valid():
            senha = gararSenhaAleatoria()
            retono = formCriacaoUsuario.save(senha)
            
            if retono is not None:
                mandar_email(email=retono.email, tipo='criacaoADM', usuario=retono, senha=senha, usuarioADM=request.user)
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