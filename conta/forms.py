from django import forms
from .models import Usuario
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class FormLogin(forms.Form):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'id': 'matricula', 'placeholder': 'matrícula'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'senha', 'placeholder': 'senha'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark','name': 'captcha'}))

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if not matricula.isdigit():
            raise forms.ValidationError('A matrícula deve conter apenas números.')
        elif Usuario.objects.filter(matricula=matricula).count() == 0:
            raise forms.ValidationError('Usuário não encontrado.')
        return matricula

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 6:
            raise forms.ValidationError('A senha deve conter pelo menos 6 caracteres.')
        return senha
    
    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        if not captcha:
            raise forms.ValidationError('Você deve marcar a caixa de verificação.')
        return captcha
    
    