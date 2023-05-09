import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from home.models import Solicitacao
from conta.models import Usuario
from faker import Faker

fake = Faker('pt_BR')

def popular_solicitacao():
    quantidade = None
    tentativas = 0
    while True:
        if tentativas == 3:
            print('Número máximo de tentativas alcançado!')
            break
        try:
            quantidade = int(input('Quantas solicitações você deseja criar? '))
            break
        except ValueError:
            print('Digite um número inteiro!')
            tentativas += 1
            continue
        
    if quantidade is not None:  
        for x in range(quantidade):
            nome = fake.first_name()
            sobrenome = fake.last_name()
            cpf = fake.cpf()
            email = fake.email()
            motivo = fake.text()
            usuario = Usuario.objects.get(id=1)
            while True:
                if not Solicitacao.objects.filter(cpf=cpf).exists():
                    break
                else:
                    cpf = fake.cpf()
                
            while True:
                if not Solicitacao.objects.filter(email=email).exists():
                    break
                else:
                    email = fake.email()
                    
            solicitacao = Solicitacao.objects.create(
                nome=nome,
                sobrenome=sobrenome,
                cpf=cpf,
                email=email,
                motivo=motivo,
                usuario=usuario
            )
            
            print(f'N° {x+1} Solicitação {solicitacao} criada com sucesso!')
        
popular_solicitacao()

