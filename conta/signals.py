from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Usuario
import re

@receiver(post_save, sender=Usuario)
def gerar_usuario(sender, instance, created, **kwargs):
    if created:
        if instance.username == None or instance.username == '':
            username = instance.get_full_name()
            contador = 1
            
            while True:
                if User.objects.filter(username=username).exists():
                    username = re.sub(r'\d+$', '', username)
                    username = username + str(contador)
                    contador += 1
                else:
                    break
            instance.username = username

 
@receiver(post_save, sender=Usuario)
def criar_matricula(sender, instance, created, **kwargs):
    if created:
        if instance.matricula == None or instance.matricula == '':
            instance.matricula = instance.id.__str__().zfill(6)
            instance.save()
                
