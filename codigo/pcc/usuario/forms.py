from django import forms 
from .models import Usuario

class AdicionarUsuario(forms.ModelForm):
    class Meta:
        model= Usuario
        fields = ('nome', 'sobrenome', 'email','telefone', 'imagem')
