from django import forms 
from .models import ONG

class AdicionarONG(forms.ModelForm):
    class Meta:
        model= ONG
        fields = ('nome', 'email','telefone', 'UF', 'cidade', 'rua', 'numero', 'bairro', 'imagem')
