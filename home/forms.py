from django import forms
from .models import Solicitacao
from validate_cpf import validate_cpf

class FormSolicitacaoMatricula(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome:'}))
    sobrenome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sobrenome:'}))
    cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': 'CPF:', 'id': 'cpf-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail:'}))
    
    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip().lower()
        return nome

    def clean_sobrenome(self):
        sobrenome = self.cleaned_data['sobrenome'].strip().lower()
        return sobrenome
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf'].strip()
        if Solicitacao.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já cadastrado!')
        elif not validate_cpf.is_valid(cpf):
            raise forms.ValidationError('CPF inválido!')
        return cpf
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if Solicitacao.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email
    
    def save(self, usuario):
        try:
            soli = Solicitacao.objects.create(
                nome=self.cleaned_data['nome'],
                sobrenome=self.cleaned_data['sobrenome'],
                cpf=self.cleaned_data['cpf'],
                email=self.cleaned_data['email'],
                usuario=usuario
            )
        except:
            raise forms.ValidationError('Erro ao salvar solicitação!')
        return soli
    