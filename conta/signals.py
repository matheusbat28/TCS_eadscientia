from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Usuario, Token
import re
from unidecode import unidecode

@receiver(post_save, sender=Usuario)
def gerar_usuario(sender, instance, created, **kwargs):
    if created:
        if instance.username == None or instance.username == '':
            usuario = unidecode(instance.get_full_name().lower().replace(' ', ''))
            
            count = 1
            while Usuario.objects.filter(username=usuario).exists():
                usuario = re.sub(r'\d+', '', usuario)
                usuario = usuario + str(count)
                count += 1
            instance.username = usuario
            instance.save()
 
@receiver(post_save, sender=Usuario)
def criar_matricula(sender, instance, created, **kwargs):
    if created:
        if instance.matricula == None or instance.matricula == '':
            instance.matricula = instance.id.__str__().zfill(6)
            instance.save()
        
                
