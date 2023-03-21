from django import forms
from .models import Usuario
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class UsuarioForm(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'id': 'matricula', 'placeholder': 'matrícula'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'senha', 'placeholder': 'senha'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Usuario
        fields = ['matricula','senha']