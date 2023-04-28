from django.test import TestCase
from .models import Usuario
from faker import Faker
from cpf_generator import CPF

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.cpf = None
        self.email = None
        self.senha = 'Anakim3242'
        
        while True:
            cpf = CPF.generate()
            if not Usuario.objects.filter(cpf=cpf).exists():
                break
            
            
        while True:
            email = self.faker.email()
            if not Usuario.objects.filter(email=email).exists():
                break
                
        self.usuario = Usuario.objects.create(
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            cpf=cpf,
            email=self.faker.email(),
            password=self.senha
        )
        
    def test_criar_usuario(self):
        self.assertTrue(Usuario.objects.exists())
        