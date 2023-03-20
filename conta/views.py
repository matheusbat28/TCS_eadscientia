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
        usuarioVerificado = auth.authenticate(request, username=matricula, password=senha)
        if usuarioVerificado is not None:
            auth.login(request, usuarioVerificado)
            return redirect('home')
        else:
            messages.error(request, 'Matrícula ou senha inválidos.')

        return render(request, 'conta/index.html', {'form': form})
    else:
        return render(request, 'conta/index.html', {'form': form})
