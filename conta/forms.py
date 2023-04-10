from django import forms
from .models import Usuario
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
import re

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
        senha = self.cleaned_data['senha']
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


class FormVerificarCodigo(forms.Form):
    codigo_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'codigo', 'placeholder': '0'}), required=False, max_length=1)
    codigo_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'codigo', 'placeholder': '0'}), required=False, max_length=1)
    codigo_3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'codigo', 'placeholder': '0'}), required=False, max_length=1)
    codigo_4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'codigo', 'placeholder': '0'}), required=False, max_length=1)
    codigo_5 = forms.CharField(widget=forms.TextInput(attrs={'class': 'codigo', 'placeholder': '0'}), required=False, max_length=1)
    codigo_6 = forms.CharField(widget=forms.TextInput(attrs={'class': 'codigo', 'placeholder': '0'}), required=False, max_length=1)
    
    def clean_codigo_1(self):
        codigo_1 = self.cleaned_data['codigo_1'].strip()
        if len(codigo_1) == 0:
            raise forms.ValidationError('Você deve informar o código.')
        elif not codigo_1.isdigit():
            raise forms.ValidationError('O código deve conter apenas números.')
        return codigo_1
    
    def clean_codigo_2(self):
        codigo_2 = self.cleaned_data['codigo_2'].strip()
        if len(codigo_2) == 0:
            raise forms.ValidationError('Você deve informar o código.')
        elif not codigo_2.isdigit():
            raise forms.ValidationError('O código deve conter apenas números.')
        return codigo_2 
    
    def clean_codigo_3(self):
        codigo_3 = self.cleaned_data['codigo_3'].strip()
        if len(codigo_3) == 0:
            raise forms.ValidationError('Você deve informar o código.')
        elif not codigo_3.isdigit():
            raise forms.ValidationError('O código deve conter apenas números.')
        return codigo_3
    
    def clean_codigo_4(self):
        codigo_4 = self.cleaned_data['codigo_4'].strip()
        if len(codigo_4) == 0:
            raise forms.ValidationError('Você deve informar o código.')
        elif not codigo_4.isdigit():
            raise forms.ValidationError('O código deve conter apenas números.')
        return codigo_4
    
    def clean_codigo_5(self):
        codigo_5 = self.cleaned_data['codigo_5'].strip()
        if len(codigo_5) == 0:
            raise forms.ValidationError('Você deve informar o código.')
        elif not codigo_5.isdigit():
            raise forms.ValidationError('O código deve conter apenas números.')
        return codigo_5
    
    def clean_codigo_6(self):
        codigo_6 = self.cleaned_data['codigo_6'].strip()
        if len(codigo_6) == 0:
            raise forms.ValidationError('Você deve informar o código.')
        elif not codigo_6.isdigit():
            raise forms.ValidationError('O código deve conter apenas números.')
        return codigo_6

        
class FormAlterarSenha(forms.Form):
    senha1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder': 'senha:'}), required=False)
    senha2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder': 'senha novamente:'}), required=False)
    
    def clean_senha1(self):
        senha1 = self.cleaned_data['senha1'].strip()
        if len(senha1) == 0:
            raise forms.ValidationError('Você deve informar a senha.')
        elif len(senha1) < 6:
            raise forms.ValidationError('A senha deve conter pelo menos 6 caracteres.')
        elif re.search('[0-9]', senha1) is None:
            raise forms.ValidationError('A senha deve conter pelo menos um número.')
        elif re.search('[A-Z]', senha1) is None:
            raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula.')
        elif re.search('[a-z]', senha1) is None:
            raise forms.ValidationError('A senha deve conter pelo menos uma letra.')
        return senha1
    
    def clean_senha2(self):
        senha2 = self.cleaned_data['senha2'].strip()
        if len(senha2) == 0:
            raise forms.ValidationError('Você deve informar a senha novamente.')
        elif len(senha2) < 6:
            raise forms.ValidationError('A senha deve conter pelo menos 6 caracteres.')
        elif re.search('[0-9]', senha2) is None:
            raise forms.ValidationError('A senha deve conter pelo menos um número.')
        elif re.search('[A-Z]', senha2) is None:
            raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula.')
        elif re.search('[a-z]', senha2) is None:
            raise forms.ValidationError('A senha deve conter pelo menos uma letra.')
        return senha2