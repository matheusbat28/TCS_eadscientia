from django import forms
from .models import Usuario
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox, ReCaptchaV3

class UsuarioForm(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'id': 'matricula', 'placeholder': 'matrícula'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'senha', 'placeholder': 'senha'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark'}))
    class Meta:
        model = Usuario
        fields = ['matricula','senha']