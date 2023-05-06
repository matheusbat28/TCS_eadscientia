from django.shortcuts import render

def adicionarCurso(request):
    return render(request, 'adicionarCurso/index.html')
