from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import FormLogin, FormRecuperarSenha, FormVerificarCodigo, FormAlterarSenha
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from random import randint
from .models import Usuario, Token
from django.contrib.auth.hashers import make_password, check_password


def login(request):
    formLogin = FormLogin(request.POST)
    formRecuperarSenha = FormRecuperarSenha(request.POST)
    if request.method == 'POST' and 'btn-entrar' in request.POST:
        if formLogin.is_valid():
            usuario = auth.authenticate(username=formLogin.cleaned_data['matricula'], password=formLogin.cleaned_data['senha'])
            if usuario is not None and usuario.is_active and usuario.last_login is not None:
                if usuario.is_active and usuario.last_login is not None:
                    auth.login(request, usuario)
                    return redirect('home')
                else:
                    messages.error(request, 'Usuário desativado.')
                    return redirect('login')
            if usuario is not None and usuario.last_login is None:
                auth.login(request, usuario)
                return redirect('recuperar_senha', id=usuario.id)
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                return redirect('login')
        else:
            json = formLogin.errors.as_json()

            if 'matricula' in json:
                messages.error(request, formLogin.errors['matricula'][0])
                return redirect('login')
            elif 'senha' in json:
                messages.error(request, formLogin.errors['senha'][0])
                return redirect('login')   
            elif 'captcha' in json:
                messages.error(request, formLogin.errors['captcha'][0])
                return redirect('login')
    
    elif request.method == 'POST' and 'btn-recuperar-senha' in request.POST:
        if formRecuperarSenha.is_valid():
            token = gerar_token()
            
            if Token.objects.filter(usuario=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email'])).exists():
                Token.objects.filter(usuario=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email'])).delete()           
            Token.objects.create(token=make_password(token), usuario=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email']))
                
            mandar_email(formRecuperarSenha.cleaned_data['email'], token)
            messages.success(request, f'Código enviado para o email {formRecuperarSenha.cleaned_data["email"]}')
            return redirect('verificar_codigo', id=Usuario.objects.get(email=formRecuperarSenha.cleaned_data['email']).id)
        else:
            json = formRecuperarSenha.errors.as_json()

            if 'email' in json:
                messages.error(request, formRecuperarSenha.errors['email'][0])
                return redirect('login')
            elif 'captcha' in json:
                messages.error(request, formRecuperarSenha.errors['captcha'][0])
                return redirect('login')

    return render(request, 'conta/index.html', {'formLogin': formLogin, 'formRecuperarSenha': formRecuperarSenha})

def logout(request):
    auth.logout(request)
    return redirect('login')


def verificar_codigo(request, id):
    formVerificarCodigo = FormVerificarCodigo(request.POST)
    if request.method == 'POST' and 'btn-verificar-codigo' in request.POST:
        if formVerificarCodigo.is_valid():
            codigo = f'{formVerificarCodigo.cleaned_data["codigo_1"]}{formVerificarCodigo.cleaned_data["codigo_2"]}{formVerificarCodigo.cleaned_data["codigo_3"]}{formVerificarCodigo.cleaned_data["codigo_4"]}{formVerificarCodigo.cleaned_data["codigo_5"]}{formVerificarCodigo.cleaned_data["codigo_6"]}'
            if Token.objects.filter(usuario=Usuario.objects.get(id=id)).exists():
                if check_password(codigo, Token.objects.get(usuario=Usuario.objects.get(id=id)).token):
                    Token.objects.filter(usuario=Usuario.objects.get(id=id)).update(validou=True)
                    return redirect('recuperar_senha', id=id)
            else:
                messages.error(request, 'Código inválido.')
                return redirect('verificar_codigo', id=id)
        else:
            json = formVerificarCodigo.errors.as_json()
            
            if 'codigo_1' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_1'][0])
                return redirect('verificar_codigo', id=id)
            elif 'codigo_2' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_2'][0])
                return redirect('verificar_codigo', id=id)
            elif 'codigo_3' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_3'][0])
                return redirect('verificar_codigo', id=id)
            elif 'codigo_4' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_4'][0])
                return redirect('verificar_codigo', id=id)
            elif 'codigo_5' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_5'][0])
                return redirect('verificar_codigo', id=id)
            elif 'codigo_6' in json:
                messages.error(request, formVerificarCodigo.errors['codigo_6'][0])
                return redirect('verificar_codigo', id=id)
                
    elif request.method == 'POST' and 'btn-reenviar-codigo' in request.POST:
        Token.objects.filter(usuario=Usuario.objects.get(id=id)).delete()
        token = gerar_token()
        Token.objects.create(token=make_password(token), usuario=Usuario.objects.get(id=id))
        mandar_email(Usuario.objects.get(id=id).email, token)
        messages.success(request, f'Código enviado para o email {Usuario.objects.get(id=id).email}') 
        return redirect('verificar_codigo', id=id)
        
                               
    if Token.objects.filter(usuario=Usuario.objects.get(id=id), validou=False).exists():
        return render(request, 'verificar_codigo/index.html', {'formVerificarCodigo': formVerificarCodigo})
    else:
        messages.error(request, 'Não solicitou a recuperação de senha.')
        return redirect('login')

def mandar_email(email, token):
    email = EmailMultiAlternatives('Recuperação de Senha', f'token {token}', settings.EMAIL_HOST_USER, [email])
    email.send()

def gerar_token():
    token = str(randint(100000, 999999))
    while True:
        if Token.objects.filter(token=make_password(token)).exists():
            token = str(randint(100000, 999999))
        else:
            break
    return token

def recuperar_senha(request, id):
    formAlterarSenha = FormAlterarSenha(request.POST)
    
    if request.method == 'POST':
        if formAlterarSenha.is_valid():
            if formAlterarSenha.cleaned_data['senha1'] == formAlterarSenha.cleaned_data['senha2']:
                usuario = Usuario.objects.get(id=id)
                usuario.set_password(formAlterarSenha.cleaned_data['senha1'])
                usuario.save()
                Token.objects.filter(usuario=Usuario.objects.get(id=id)).delete()
                messages.success(request, 'Senha alterada com sucesso.')
                return redirect('login')
               
            else:
                messages.error(request, 'As senhas não são iguais.')
        else:
            json = formAlterarSenha.errors.as_json()
            
            if 'senha1' in json:
                messages.error(request, formAlterarSenha.errors['senha1'][0])
                return redirect('recuperar_senha', id=id)
            elif 'senha2' in json:
                messages.error(request, formAlterarSenha.errors['senha2'][0])
                return redirect('recuperar_senha', id=id)
                    
    if Token.objects.filter(usuario=Usuario.objects.get(id=id), validou=True).exists():
        return render(request, 'redefinir_senha/index.html', {'formAlterarSenha': formAlterarSenha})
    elif Usuario.objects.filter(id=id, is_active=True, last_login__isnull=False).exists():
        print('entrou')
        return render(request, 'redefinir_senha/index.html', {'formAlterarSenha': formAlterarSenha})
    else:
        messages.error(request, 'Não solicitou a recuperação de senha.')
        return redirect('login')
    