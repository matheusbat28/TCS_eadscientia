from django import forms
from conta.models import Usuario
from curso.models import Curso, SolicitarCurso

class FormSolicitarCurso(forms.Form):
    aluno = forms.CharField(widget=forms.TextInput(attrs={'id': 'aluno', 'placeholder': 'aluno', 'readonly': 'readonly'}), required=True)
    curso = forms.CharField(widget=forms.TextInput(attrs={'id': 'curso', 'placeholder': 'curso', 'readonly': 'readonly'}), required=True)
    motivo = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'motivo', 'placeholder': 'motivo'}),
        required=True
    )
    
    def clean_aluno(self):
        aluno = self.cleaned_data['aluno'].strip()
        
        if not Usuario.objects.filter(username = aluno).exists():
            raise forms.ValidationError(f'Usuário {aluno} não existe')
        elif len(aluno) == 0:
            raise forms.ValidationError(f'Usuário não pode ser vazio')
        return aluno
         
    def clean_curso(self):
        curso = self.cleaned_data['curso'].strip()
        
        if not Curso.objects.filter(nome = curso):
            raise forms.ValidationError(f'{curso} não existe')
        elif len(curso) == 0:
            raise forms.ValidationError(f'Curso não pode ser vazio')
        return curso
        
    def clean_motivo(self):
        motivo = self.cleaned_data['motivo'].strip()
        
        if len(motivo) == 0:
            raise forms.ValidationError(f'Motivo não pode ser vazio')
        return motivo
        
    def save(self, id_curso):
        try:
            soli = SolicitarCurso.objects.create(
                aluno = Usuario.objects.get(username = self.clean_aluno()),
                curso = Curso.objects.get(id = id_curso),
                motivo = self.clean_motivo()
                    
            )
        except:
            raise forms.ValidationError('Erro ao salvar solicitação do curso!')
        
        return soli