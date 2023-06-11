from django import template
from datetime import datetime


register = template.Library()

@register.filter
def in_grups(user, group_name):
    return user.groups.filter(name=group_name.strip()).exists()

@register.filter
def massage_in_time(usuario):
    horaAtual = datetime.now().hour
    if horaAtual >= 0 and horaAtual < 12:
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
    quant = curso.quantidade_assitido
    cont = 0
    for video in curso.curso.capitulos.all():
        cont += video.videos.all().count()  
    return round((quant / cont) * 100)

@register.filter
def falta_dia(data):
    diferenca = data - datetime.now().replace(tzinfo=data.tzinfo)
    return f'Falta: {diferenca.days} dias'