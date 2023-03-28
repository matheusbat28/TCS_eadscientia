from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import FormLogin, FormRecuperarSenha

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
            return render(request, 'conta/index.html', {'formLogin': formLogin})
    else:
        return render(request, 'conta/index.html', {'formLogin': formLogin, 'formRecuperarSenha': formRecuperarSenha})
