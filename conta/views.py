from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm

def login(request):
    form = UsuarioForm()
    if request.method == 'POST':
        matricula = request.POST['matricula'].strip()
        senha = request.POST['senha'].strip()
        captcha = request.POST['g-recaptcha-response']

        if not captcha:
            messages.error(request, 'Por favor, confirme o captcha.')
            return render(request, 'conta/index.html', {'form': form})
        
        usuarioVerificado = auth.authenticate(request, username=matricula, password=senha)
        if usuarioVerificado is not None:
            auth.login(request, usuarioVerificado)
            return redirect('home')
        else:
            messages.error(request, 'Matrícula ou senha inválidos.')

        return render(request, 'conta/index.html', {'form': form})
    else:
        return render(request, 'conta/index.html', {'form': form})
