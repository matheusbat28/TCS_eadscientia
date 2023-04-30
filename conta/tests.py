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
        self.usuario = Usuario.objects.create(
            first_name=self.nome, 
            last_name=self.sobrenome, 
            email=self.email, 
            cpf=self.cpf, 
            password=self.senha)
    
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
        
    def test_listar_usuarios(self):
        usuarios = Usuario.objects.all()
        self.assertIsNotNone(usuarios)
        
    def test_buscar_usuario(self):
        usuario = Usuario.objects.get(cpf=self.usuario.cpf)
        self.assertIsNotNone(usuario)
        
    def test_atualizar_usuario(self):
        usuario = Usuario.objects.get(cpf=self.usuario.cpf)
        usuario.first_name = fake.first_name()
        usuario.save()
        self.assertEqual(usuario.first_name, usuario.first_name)
        
    def test_deletar_usuario(self):
        usuario = Usuario.objects.get(cpf=self.usuario.cpf)
        usuario.delete()
        self.assertFalse(Usuario.objects.filter(cpf=self.usuario.cpf).exists())
        
class TokenTestCase(TestCase):
    def setUp(self):
        self.nome = fake.first_name()
        self.sobrenome = fake.last_name()
        self.email = fake.email()
        self.cpf = CPF.generate()
        self.senha = '123456'
        self.codigo = fake.random_number(digits=6)
        self.usuario = Usuario.objects.create(
            first_name=self.nome, 
            last_name=self.sobrenome, 
            email=self.email, 
            cpf=self.cpf, 
            password=self.senha)
        self.token = Token.objects.create(usuario=self.usuario, token=self.codigo)
        
        
    def test_criar_token(self):
        self.token.delete()
        self.token = Token.objects.create(usuario=self.usuario, token=self.codigo)
        self.assertIsNotNone(self.token)
        
    def test_listar_tokens(self):
        tokens = Token.objects.all()
        self.assertIsNotNone(tokens)
        
    def test_buscar_token(self):
        token = Token.objects.get(usuario=self.usuario)
        self.assertIsNotNone(token)
        
    def test_atualizar_token(self):
        token = Token.objects.get(usuario=self.usuario)
        token.validou = True
        token.save()
        self.assertTrue(token.validou)
        
    def test_deletar_token(self):
        token = Token.objects.get(usuario=self.usuario)
        token.delete()
        self.assertFalse(Token.objects.filter(usuario=self.usuario).exists())
        
        

        