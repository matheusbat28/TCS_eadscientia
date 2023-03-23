from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import FormLogin

def login(request):
    form = FormLogin(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            usuario = auth.authenticate(username=form.cleaned_data['matricula'], password=form.cleaned_data['senha'])
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('home')
        else:
            json = form.errors.as_json()

            if 'matricula' in json:
                messages.error(request, form.errors['matricula'][0])
            elif 'senha' in json:
                messages.error(request, form.errors['senha'][0])
            elif 'captcha' in json:
                messages.error(request, form.errors['captcha'][0])
    return render(request, 'conta/index.html', {'form': form})

