from django.test import TestCase
from .models import Usuario, Token
from django.contrib.auth.models import  Group
from faker import Faker
from cpf_generator import CPF

fake = Faker('pt_BR')

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.nome = fake.first_name()
        self.sobrenome = fake.last_name()
        self.email = fake.email()
        self.cpf = CPF.generate()
        self.senha = '123456'
    
    
    def test_criar_usuario(self):
        while Usuario.objects.filter(cpf=self.cpf).exists():
            self.cpf = CPF.generate()
        
        while Usuario.objects.filter(email=self.email).exists():
            self.email = fake.email() 
                      
        usuario = Usuario.objects.create(
            first_name=self.nome,
            last_name=self.sobrenome,
            email=self.email,
            cpf=self.cpf, 
            password=self.senha) 
               
        self.assertIsNotNone(usuario)
        return usuario
        
    def test_listar_usuarios(self):
        usuarios = Usuario.objects.all()
        self.assertIsNotNone(usuarios)
        
    def test_buscar_usuario(self):
        usuario = self.test_criar_usuario()
        self.assertIsNotNone(usuario)
        
    def test_atualizar_usuario(self):
        usuario = self.test_criar_usuario()
        usuario.first_name = fake.first_name()
        usuario.save()
        self.assertEqual(usuario.first_name, usuario.first_name)
        
    def test_deletar_usuario(self):
        usuario = self.test_criar_usuario()
        usuario.delete()
        self.assertFalse(Usuario.objects.filter(cpf=usuario.cpf).exists())
        
class TokenTestCase(TestCase):
    def setUp(self):
        self.nome = fake.first_name()
        self.sobrenome = fake.last_name()
        self.email = fake.email()
        self.cpf = CPF.generate()
        self.senha = '123456'
        self.codigo = fake.random_number(digits=6)
        self.usuario = UsuarioTestCase.test_criar_usuario(self)
        
        
    def test_criar_token(self):
        token = Token.objects.create(usuario=self.usuario, token=self.codigo)
        self.assertIsNotNone(token)
        return token
        
    def test_listar_tokens(self):
        tokens = Token.objects.all()
        self.assertIsNotNone(tokens)
        
    def test_buscar_token(self):
        token = self.test_criar_token()
        self.assertIsNotNone(token)
        
    def test_atualizar_token(self):
        token = self.test_criar_token()
        token.validou = True
        token.save()
        self.assertTrue(token.validou)
        
    def test_deletar_token(self):
        token = self.test_criar_token()
        token.delete()
        self.assertFalse(Token.objects.filter(token=token.token).exists())
        
        

        