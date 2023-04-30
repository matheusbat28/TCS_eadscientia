from django.test import TestCase
from .models import Solicitacao
from conta.models import Usuario
from faker import Faker
from cpf_generator import CPF

fake = Faker('pt_BR')

class SolicitacaoTestCase(TestCase):
    def setUp(self):
        self.nome = fake.first_name()
        self.sobrenome = fake.last_name()
        self.cpf = CPF.generate()
        self.email = fake.email()
        self.motivo = fake.text()
        self.usuario = Usuario.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            cpf=CPF.generate(),
            email=fake.email(),
            password='123456',
        )
        
    def test_criar_solicitacao(self):
        while Usuario.objects.filter(cpf=self.cpf).exists():
            self.cpf = CPF.generate()
        
        while Usuario.objects.filter(email=self.email).exists():
            self.email = fake.email()  
            
        solicitacao = Solicitacao.objects.create(
            nome=self.nome,
            sobrenome=self.sobrenome,
            cpf=self.cpf,
            email=self.email,
            usuario=self.usuario,
            motivo=self.motivo,
        )
        self.assertIsNotNone(solicitacao)
        return solicitacao
    
    def test_listar_solicitacoes(self):
        solicitacoes = Solicitacao.objects.all()
        self.assertIsNotNone(solicitacoes)
        
    def test_buscar_solicitacao(self):
        solicitacao = self.test_criar_solicitacao()
        solicitacao = Solicitacao.objects.get(cpf=solicitacao.cpf)
        
    def test_atualizar_solicitacao(self):
        solicitacao = self.test_criar_solicitacao()
        solicitacao.nome = fake.first_name()
        solicitacao.save()
        self.assertEqual(solicitacao.nome, solicitacao.nome)
        
    def test_deletar_solicitacao(self):
        solicitacao = self.test_criar_solicitacao()
        solicitacao.delete()
        self.assertFalse(Solicitacao.objects.filter(cpf=solicitacao.cpf).exists())