from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Solicitacao
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

@receiver(post_save, sender=Solicitacao)
def mandar_email_criacao(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string('email/solicitacaoMatricula.html', {'solicitacao': instance}) 
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'Solicitação de conta',
            text_content,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RH]
            )
        email.attach_alternative(html_content, "text/html")
        email.send()
        
@receiver(post_delete, sender=Solicitacao)
def mandar_email_exclusao(sender, instance, **kwargs):
    if instance.criado:
        pass
    else:
        html_content = render_to_string('email/deletar.html', {'solicitacao': instance})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'solicitação de matrícula excluída',
            text_content,
            settings.EMAIL_HOST_USER,
            [instance.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()