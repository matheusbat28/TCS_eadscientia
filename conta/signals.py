from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Usuario, Token
import re
from unidecode import unidecode
import string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import random

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

@receiver(post_save, sender=Usuario)
def criar_senha(sender, instance, created, **kwargs):
    if created:
        if instance.password == None or instance.password == '':
            letra = string.ascii_letters  
            numero = string.digits
            caracteres = letra + numero
            senha = ''.join(random.choice(caracteres) for i in range(8))
            
            instance.set_password(senha)
            instance.save()
            
            html_content = render_to_string('email/aprovar.html', {'usuario': instance, 'senha': senha}) 
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                'Aprovação de cadastro',
                text_content,
                settings.EMAIL_HOST_USER,
                [instance.email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
                
