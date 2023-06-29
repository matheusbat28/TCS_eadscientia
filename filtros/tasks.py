from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from curso.models import AcessoCursoUsuario
from django.utils import timezone

def remover_curso_negativo():
    for acesso in AcessoCursoUsuario.objects.all():
        diff = acesso.data_termino - timezone.now()
        if diff.total_seconds() <= 0:
            acesso.delete()
    
    
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(remover_curso_negativo, CronTrigger(hour=4, minute=0))
    scheduler.start()