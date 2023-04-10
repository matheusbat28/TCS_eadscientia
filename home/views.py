from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormSolicitacaoMatricula
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Solicitacao
from conta.models import Usuario
from django.core.paginator import Paginator
import random
import string

@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
def solicitacaomMatricula(request):
    formFormSolicitacaoMatricula = FormSolicitacaoMatricula(request.POST)
    
    if request.method == 'POST':
        if formFormSolicitacaoMatricula.is_valid():
            solicitacao = formFormSolicitacaoMatricula.save(request.user)
            if solicitacao is not None:
                mandar_email(settings.EMAIL_RH, solicitacao, 'solicitacao')
                messages.success(request, 'Solicitação enviada com sucesso.')
                return redirect('solicitacaomMatricula')
            
        else:
            json = formFormSolicitacaoMatricula.errors.as_json()

            if 'nome' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['nome'][0])
                return redirect('solicitacaomMatricula')
            elif 'sobrenome' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['sobrenome'][0])
                return redirect('solicitacaomMatricula')
            elif 'cpf' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['cpf'][0])
                return redirect('solicitacaomMatricula')
            elif 'email' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['email'][0])
                return redirect('solicitacaomMatricula')
            elif 'curso' in json:
                messages.error(request, formFormSolicitacaoMatricula.errors['curso'][0])
                return redirect('solicitacaomMatricula')
                
    return render(request, 'socilitarMatricula/index.html', {'formFormSolicitacaoMatricula': formFormSolicitacaoMatricula})


     
@login_required
def listarSolicitarMatricula(request):
    solicitacoes = Solicitacao.objects.filter(criado=False).order_by('sobrenome').order_by('nome')
    paginator = Paginator(solicitacoes, 10)
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'listarSolicitarMatricula/index.html', {'posts': posts})

@login_required
def visualizarSolicitacao(request, id):
    if request.method == 'POST' and 'btnVoltar' in request.POST:
        return redirect('listarSolicitarMatricula')
    elif request.method == 'POST' and 'btnAprovar' in request.POST:
        solicitacao = Solicitacao.objects.get(id=id)
        if solicitacao is not None:
            if Usuario.objects.filter(matricula=solicitacao.cpf).exists():
                messages.error(request, 'Já existe um usuário com esse CPF.')
                return redirect('visualizarSolicitacao', id=id)
            elif Usuario.objects.filter(email=solicitacao.email).exists():
                messages.error(request, 'Já existe um usuário com esse email.')
                return redirect('visualizarSolicitacao', id=id)
            else:
                try:
                    senha = gararSenhaAleatoria()
                    usuario = Usuario.objects.create_user( email=solicitacao.email, 
                                                            cpf=solicitacao.cpf, 
                                                            first_name=solicitacao.nome, 
                                                            last_name=solicitacao.sobrenome, 
                                                            username=solicitacao.nome.lower().replace(' ', '') + solicitacao.sobrenome.lower().replace(' ', ''),
                                                            )
                    usuario.cursos.add(solicitacao.curso)
                    usuario.set_password(senha)
                    usuario.save()
                    solicitacao.criado = True
                    solicitacao.save()
                
                except Exception:
                    messages.error(request, 'Erro ao criar o usuário.')
                    return redirect('visualizarSolicitacao', id=id)
                    
                messages.success(request, 'Solicitação aprovada com sucesso.')
                return redirect('listarSolicitarMatricula')

        else:
            messages.error(request, 'Erro ao aprovar a solicitação.')
            return redirect('listarSolicitarMatricula')
    return render(request, 'visualizacaoSolicitacaoMatricula/index.html', {'solicitacao': Solicitacao.objects.get(id=id)})


@login_required
def deletarSolicitacao(request, id):
    Solicitacao.objects.get(id=id).delete()
    return redirect('listarSolicitarMatricula')

def gararSenhaAleatoria():
    letras = string.ascii_letters
    numeros = string.digits
    caracteres = letras + numeros
    senha = ''.join(random.choice(caracteres) for i in range(8))
    return senha

def mandar_email(email, solicitacao, tipo):
    
    if tipo == 'solicitacao':
        email = EmailMultiAlternatives(f'solicitação de matricula {solicitacao.nome.title()} {solicitacao.sobrenome.title()}', f'''
                            Solicitação de matricula
                Nome: {solicitacao.nome.title()} {solicitacao.sobrenome.title()}
                cpf: {solicitacao.cpf}
                Email: {solicitacao.email}
                Curso: {solicitacao.curso.nome.title()}
                Quem solicitou: {solicitacao.usuario.get_full_name().title()} ({solicitacao.usuario.matricula})
                
                                    ''', settings.EMAIL_HOST_USER, [email])
        email.send()
    elif tipo == 'aprovacao':
        email = EmailMultiAlternatives(f'Aprovação da matricula {solicitacao.nome.title()} {solicitacao.sobrenome.title()}', f'''
                            Aprovação da matricula
                Nome: {solicitacao.nome.title()} {solicitacao.sobrenome.title()}
                cpf: {solicitacao.cpf}
                Email: {solicitacao.email}
                Curso: {solicitacao.curso.nome.title()}
                Quem solicitou: {solicitacao.usuario.get_full_name().title()} ({solicitacao.usuario.matricula})
                
                                    ''', settings.EMAIL_HOST_USER, [email])
        email.send()