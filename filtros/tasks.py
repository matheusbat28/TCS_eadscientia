from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from curso.models import AcessoCursoUsuario
from conta.models import Token
from django.utils import timezone

def remover_curso_negativo():
    for acesso in AcessoCursoUsuario.objects.all():
        diff = acesso.data_termino - timezone.now()
        if diff.total_seconds() <= 0:
            acesso.delete()
            
def remover_token():
    for token in Token.objects.all():
        time_difference = timezone.now() - token.data_criacao
        print('entrou')
        if time_difference.total_seconds() >= 900:
            token.delete()
    
    
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(remover_curso_negativo, CronTrigger(hour=4, minute=0))
    scheduler.add_job(remover_token, 'interval', minutes=1)
    scheduler.start()