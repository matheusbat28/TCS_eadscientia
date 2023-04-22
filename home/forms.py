from django import forms
from .models import Solicitacao
from curso.models import Curso
from conta.models import Usuario
from django.contrib.auth.models import Group
from validate_cpf import validate_cpf

class FormSolicitacaoMatricula(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome:'}))
    sobrenome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sobrenome:'}))
    cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': 'CPF:', 'id': 'cpf-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail:'}))
    motivo = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Motivo:', 'cols': '30', 'rows': '7'}))
    
    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip().lower()
        return nome

    def clean_sobrenome(self):
        sobrenome = self.cleaned_data['sobrenome'].strip().lower()
        return sobrenome
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf'].strip()
        if Solicitacao.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já solicitou a matrícula!')
        elif Usuario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já cadastrado!')
        elif not validate_cpf.is_valid(cpf):
            raise forms.ValidationError('CPF inválido!')
        return cpf
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if Solicitacao.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já solicitou a matricula!')
        elif Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email
    
    def clean_motivo(self):
        motivo = self.cleaned_data['motivo'].strip()
        if len(motivo) == 0:
            raise forms.ValidationError('Motivo não pode ser vazio!')
        return motivo
    
    
    def save(self, usuario):
        try:
            soli = Solicitacao.objects.create(
                nome=self.cleaned_data['nome'],
                sobrenome=self.cleaned_data['sobrenome'],
                cpf=self.cleaned_data['cpf'],
                email=self.cleaned_data['email'],
                usuario=usuario,
                motivo=self.cleaned_data['motivo'],
            )
        except:
            raise forms.ValidationError('Erro ao salvar solicitação!')
        return soli
    
class FormCriacaoUsuario(forms.Form):
   nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome:'}))
   sobrenome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sobrenome:'}))
   cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': 'CPF:', 'id': 'cpf-input'}))
   email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail:'}))
   cursos = forms.ModelChoiceField(queryset=Curso.objects.all(), empty_label='Selecione um curso')
   grupos = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label='Selecione um grupo')
   
   def clean_nome(self):
       nome = self.cleaned_data['nome'].strip().lower()
       return nome
   
   def clean_sobrenome(self):
       sobrenome = self.cleaned_data['sobrenome'].strip().lower()
       return sobrenome
   
   def clean_cpf(self):
       cpf = self.cleaned_data['cpf'].strip()
       if Usuario.objects.filter(cpf=cpf).exists():
           raise forms.ValidationError('CPF já cadastrado!')
       if Solicitacao.objects.filter(cpf=cpf).exists():
           raise forms.ValidationError('CPF já solicitou a matrícula espere a aprovação pelo RH!')
       elif not validate_cpf.is_valid(cpf):
           raise forms.ValidationError('CPF inválido!')
       return cpf
   
   def clean_email(self):
       email = self.cleaned_data['email'].strip()
       if Usuario.objects.filter(email=email).exists():
           raise forms.ValidationError('E-mail já cadastrado!')
       if Solicitacao.objects.filter(email=email).exists():
           raise forms.ValidationError('E-mail já solicitou a matrícula espere a aprovação pelo RH!')
       return email
   
   def save(self, senha):
       try:
           usuario = Usuario.objects.create(
               first_name=self.cleaned_data['nome'],
               last_name=self.cleaned_data['sobrenome'],
               cpf=self.cleaned_data['cpf'],
               email=self.cleaned_data['email'],
           )
           usuario.set_password(senha)
           usuario.cursos.add(self.cleaned_data['cursos'])
           usuario.groups.add(self.cleaned_data['grupos'])
           usuario.save()
       except:
           raise forms.ValidationError('Erro ao salvar usuário!')
       return usuario