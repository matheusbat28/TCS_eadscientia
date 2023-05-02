from django.shortcuts import render

def adicionarVideo(request):
    return render(request, 'adicionarVideo/index.html')
