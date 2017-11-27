from django import forms 
from .models import Curso

class ContatoForm (forms.Form):
    nome = forms.CharField(label="Nome", required=True)
    email = forms.EmailField(label="E-mail", help_text="Informe um email válido")
    mensagem = forms.CharField(label="Mensagem", widget = forms.Textarea(), required = True)

    def envia_email(self):
        print("Usuário: "+self.cleaned_data["nome"]+
        "\nE-mail: "+self.cleaned_data["email"]+
        "\nMensagem: "+self.cleaned_data["mensagem"] )

