from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import UsuarioForm

def login(request):
    form = UsuarioForm()
    if request.method == 'POST':
        matricula = request.POST['matricula'].strip()
        senha = request.POST['senha'].strip()
        captcha = request.POST['g-recaptcha-response']

        if not captcha:
            messages.error(request, 'Por favor, confirme o captcha.')
        
        usuario_verificado = auth.authenticate(request, username=matricula, password=senha)
        if usuario_verificado is not None:
            auth.login(request, usuario_verificado)
            return redirect('home')
        else:
            messages.error(request, 'Matrícula ou senha inválidos.')

        return render(request, 'conta/index.html', {'form': form})
    else:
        return render(request, 'conta/index.html', {'form': form})
