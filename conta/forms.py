from django import forms
from .models import Usuario
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class FormLogin(forms.Form):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'id': 'matricula', 'placeholder': 'matrícula'}), required=False)
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'senha', 'placeholder': 'senha'}), required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark','name': 'captcha'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'email'}), required=False)

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula'].strip()
        if len(matricula) == 0:
            raise forms.ValidationError('Você deve informar a matrícula.')
        elif not matricula.isdigit():
            raise forms.ValidationError('A matrícula deve conter apenas números.')
        elif Usuario.objects.filter(matricula=matricula).count() == 0:
            raise forms.ValidationError('Usuário não encontrado.')
        return matricula

    def clean_senha(self):
        senha = self.cleaned_data['senha'].strip()
        if len(senha) == 0:
            raise forms.ValidationError('Você deve informar a senha.')
        elif len(senha) < 6:
            raise forms.ValidationError('A senha deve conter pelo menos 6 caracteres.')
        return senha
    
    def clean_captcha(self):
        captcha = self.cleaned_data['captcha'].strip()
        if not captcha:
            raise forms.ValidationError('Você deve marcar a caixa de verificação.')
        return captcha

class FormRecuperarSenha(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'email'}), required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark','name': 'captcha'}))
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if len(email) == 0:
            raise forms.ValidationError('Você deve informar o email ao tentar recuperar a senha.')
        elif not Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Email não encontrado ao tentar recuperar a senha.')
        return email 
    
    def clean_captcha(self):
        captcha = self.cleaned_data['captcha'].strip()
        if not captcha:
            raise forms.ValidationError('Você deve marcar a caixa de verificação ao tentar recuperar a senha.')
        return captcha
    