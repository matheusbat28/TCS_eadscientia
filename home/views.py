from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormSolicitacaoMatricula
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

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
                mandar_email(settings.EMAIL_RH, solicitacao)
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
                
    return render(request, 'socilitarMatricula/index.html', {'formFormSolicitacaoMatricula': formFormSolicitacaoMatricula})




def mandar_email(email, solicitacao):
    email = EmailMultiAlternatives(f'solicitação de matricula {solicitacao.nome.title()} {solicitacao.sobrenome.title()}', f'''
                        Solicitação de matricula
            Nome: {solicitacao.nome.title()} {solicitacao.sobrenome.title()}
            cpf: {solicitacao.cpf}
            Email: {solicitacao.email}
            Quem solicitou: {solicitacao.usuario.get_full_name().title()} ({solicitacao.usuario.matricula})
            
                                   ''', settings.EMAIL_HOST_USER, [email])
    email.send()