from django import template
from datetime import datetime, time, timedelta
from django.utils import timezone

register = template.Library()

@register.filter
def in_grups(user, group_name):
    return user.groups.filter(name=group_name.strip()).exists()

@register.filter
def massage_in_time(usuario):
    horaAtual = datetime.now().hour
    if horaAtual >= 6 and horaAtual < 12:
        return f'Bom dia, {usuario.get_full_name().title()}'
    elif horaAtual >= 12 and horaAtual < 18:
        return f'Boa tarde, {usuario.get_full_name().title()}'
    else:
        return f'Boa noite, {usuario.get_full_name().title()}'
    
    
@register.filter
def count_video_in_curso(curso):  
    cont = 0
    for video in curso.capitulos.all():
        cont += video.videos.all().count()  
    return cont

@register.filter
def proc_video_in_curso(curso):  
    quant = curso.quantidade_assitido.all().count()
    cont = 0
    for video in curso.curso.capitulos.all():
        cont += video.videos.all().count()  
    return round((quant / cont) * 100)

@register.filter
def falta_dia(data):
    diff = data - timezone.now()
    if diff.total_seconds() <= 0:
            return 'estar acabado'
    return f'Falta: {diff.days} dias'

@register.filter
def duracao_video_in_curso(curso):
    total_duracao = timedelta()

    for capitulo in curso.capitulos.all():
        for video in capitulo.videos.all():
            if video.duracao:
                duracao = video.duracao
                duracao_segundos = duracao.hour * 3600 + duracao.minute * 60 + duracao.second
                duracao_timedelta = timedelta(seconds=duracao_segundos)
                total_duracao += duracao_timedelta

    # Formatar o valor para o formato "00:00:00"
    horas = total_duracao.seconds // 3600
    minutos = (total_duracao.seconds // 60) % 60
    segundos = total_duracao.seconds % 60
    duracao_formatada = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    return duracao_formatada

@register.filter
def video_assitido(id_video, videos_assistido): 
    for video in videos_assistido:        
        if video.video.id == id_video:
            return True