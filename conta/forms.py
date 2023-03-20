from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'id': 'matricula', 'placeholder': 'matrícula'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'senha', 'placeholder': 'senha'}))
    class Meta:
        model = Usuario
        fields = ['matricula','senha']