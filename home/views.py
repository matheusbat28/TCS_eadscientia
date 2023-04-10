from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FormSolicitacaoMatricula, FormCriacaoUsuario
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
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
def solicitacaomMatricula(request):
    formFormSolicitacaoMatricula = FormSolicitacaoMatricula(request.POST)
    
    if request.method == 'POST':
        if formFormSolicitacaoMatricula.is_valid():
            solicitacao = formFormSolicitacaoMatricula.save(request.user)
            if solicitacao is not None:
                mandar_email(email=settings.EMAIL_RH, solicitacao=solicitacao, tipo='solicitacao')
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
@user_passes_test(lambda u: u.groups.filter(name='rh').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def listarSolicitarMatricula(request):
    solicitacoes = Solicitacao.objects.filter(criado=False).order_by('sobrenome').order_by('nome')
    paginator = Paginator(solicitacoes, 10)
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'listarSolicitarMatricula/index.html', {'posts': posts})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='rh').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
def visualizarSolicitacao(request, id):
    if request.method == 'POST' and 'btnVoltar' in request.POST:
        return redirect('listarSolicitarMatricula')
    elif request.method == 'POST' and 'btnRecusar' in request.POST:
        try:
            solicitacao = Solicitacao.objects.get(id=id)
            solicitacao.delete()
            mandar_email(email=solicitacao.email, solicitacao=solicitacao, tipo='recusacao')
            messages.success(request, 'Solicitação recusada com sucesso.')
            return redirect('listarSolicitarMatricula')
        except Exception:
            messages.error(request, 'Erro ao recusar a solicitação.')
            return redirect('visualizarSolicitacao', id=id)
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
                    usuario.groups.add(Group.objects.get(name='aluno'))
                    usuario.save()
                    solicitacao.criado = True
                    solicitacao.save()
                    mandar_email(email=settings.EMAIL_RH, solicitacao=solicitacao, tipo='aprovacaoRH')
                    mandar_email(email=usuario.email, usuario=usuario, tipo='aprovacao', senha=senha)
                    Solicitacao.objects.get(id=id).delete()
                
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
@user_passes_test(lambda u: u.groups.filter(name='rh').exists() or u.groups.filter(name='administrativo').exists() or u.groups.filter(name='desenvolvedor').exists(), login_url='home')
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

def mandar_email(email,tipo, solicitacao=None, senha=None, usuario=None, usuarioADM=None):
    
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
        email = EmailMultiAlternatives(f'Aprovação da matricula {usuario.get_full_name()}', f'''
                            Seu dados da matricula
                Nome: {usuario.get_full_name()}
                cpf: {usuario.cpf}
                Email: {usuario.email}
                matricula: {usuario.matricula}
                Senha: {senha}
                
                                    ''', settings.EMAIL_HOST_USER, [email])
        email.send()
    elif tipo == 'aprovacaoRH':
        email = EmailMultiAlternatives(f'Aprovação da matricula {solicitacao.nome.title()} {solicitacao.sobrenome.title()}', f'''
                            Aprovação da matricula
                Nome: {solicitacao.nome.title()} {solicitacao.sobrenome.title()}
                cpf: {solicitacao.cpf}
                Email: {solicitacao.email}
                Curso: {solicitacao.curso.nome.title()}
                Quem Aprovou: {solicitacao.usuario.get_full_name().title()} ({solicitacao.usuario.matricula})
                
                                    ''', settings.EMAIL_HOST_USER, [email])
        email.send()
    elif tipo == 'recusacao':
        email = EmailMultiAlternatives(f'Recusação da matricula {solicitacao.nome.title()} {solicitacao.sobrenome.title()}', f'''
                            Recusação da matricula
                Meu desculpa falar isso mas sua matricula foi recusada 
                para o curso {solicitacao.curso.nome.title()}
                caso tenha alguma duvida entre em contato com o RH
                
                                    ''', settings.EMAIL_HOST_USER, [email])
        email.send()
    elif tipo == 'criacaoADM':
        email = EmailMultiAlternatives(f'Conta criada por {usuarioADM.get_full_name()}', f'''
                            Bem vindo a empresa EadScientia           
                Oi me chamo {usuarioADM.get_full_name()} e trabalho no cargo de {usuarioADM.groups.all()[0].name}
                na empresa EadScientia e através desse email estou te enviando sua conta de acesso:
                Nome: {usuario.get_full_name()}
                cpf: {usuario.cpf}
                Email: {usuario.email}
                Cargo: {usuario.groups.all()[0].name}
                matricula: {usuario.matricula}
                Senha: {senha}                       
                                       
                                       ''', settings.EMAIL_HOST_USER, [email])
        
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
            
    return render(request, 'criarUsuario/index.html', {'formCriacaoUsuario': formCriacaoUsuario})