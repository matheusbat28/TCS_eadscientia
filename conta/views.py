from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import FormLogin, FormRecuperarSenha, FormVerificarCodigo
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from random import randint
from .models import Usuario, Token

def login(request):
    formLogin = FormLogin(request.POST)
    formRecuperarSenha = FormRecuperarSenha(request.POST)
    if request.method == 'POST' and 'btn-entrar' in request.POST:
        if formLogin.is_valid():
            usuario = auth.authenticate(username=formLogin.cleaned_data['matricula'], password=formLogin.cleaned_data['senha'])
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            json = formLogin.errors.as_json()

            if 'matricula' in json:
                messages.error(request, formLogin.errors['matricula'][0])
            elif 'senha' in json:
                messages.error(request, formLogin.errors['senha'][0])
            elif 'captcha' in json:
                messages.error(request, formLogin.errors['captcha'][0])
    
    elif request.method == 'POST' and 'btn-recuperar-senha' in request.POST:
        if formRecuperarSenha.is_valid():
            token = gerar_token()
            
            if Token.objects.filter(usuario=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email'])).exists():
                Token.objects.filter(usuario=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email'])).delete()           
            Token.objects.create(token=token, usuario=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email']))
                
            mandar_email(formRecuperarSenha.cleaned_data['email'], token)
            return redirect('verificar_codigo', id=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email']).id)
        else:
            json = formRecuperarSenha.errors.as_json()

            if 'email' in json:
                messages.error(request, formRecuperarSenha.errors['email'][0])
            elif 'captcha' in json:
                messages.error(request, formRecuperarSenha.errors['captcha'][0])

    return render(request, 'conta/index.html', {'formLogin': formLogin, 'formRecuperarSenha': formRecuperarSenha})

def logout(request):
    auth.logout(request)
    return redirect('login')

def verificar_codigo(request, id):
    formVerificarCodigo = FormVerificarCodigo(request.POST)
    if request.method == 'POST':
        if formVerificarCodigo.is_valid():
            codigo = f'{formVerificarCodigo.cleaned_data["codigo_1"]}{formVerificarCodigo.cleaned_data["codigo_2"]}{formVerificarCodigo.cleaned_data["codigo_3"]}{formVerificarCodigo.cleaned_data["codigo_4"]}{formVerificarCodigo.cleaned_data["codigo_5"]}{formVerificarCodigo.cleaned_data["codigo_6"]}'
            if Token.objects.filter(usuario=Usuario.objects.get(id=id), token=codigo).exists():
                messages.success(request, 'Código verificado com sucesso.')
            else:
                messages.error(request, 'Código inválido.')
        else:
            json = formVerificarCodigo.errors.as_json()
            
            if 'codigo_1' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_1'][0])
            elif 'codigo_2' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_2'][0])
            elif 'codigo_3' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_3'][0])
            elif 'codigo_4' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_4'][0])
            elif 'codigo_5' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_5'][0])
            elif 'codigo_6' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_6'][0])
                
        return render(request, 'verificar_codigo/index.html', {'formVerificarCodigo': formVerificarCodigo})
    if Token.objects.filter(usuario=Usuario.objects.get(id=id)).exists():
        return render(request, 'verificar_codigo/index.html', {'formVerificarCodigo': formVerificarCodigo})
    else:
        messages.error(request, 'Não solicitou a recuperação de senha.')
        return redirect('login')

def mandar_email(email, token):
    email = EmailMultiAlternatives('Recuperação de Senha', f'token {token}', settings.EMAIL_HOST_USER, [email])
    email.send()

def gerar_token():
    return randint(100000, 999999)