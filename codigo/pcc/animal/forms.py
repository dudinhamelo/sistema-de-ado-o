from django import forms 
from .models import Animal

class AdicionarAnimal(forms.ModelForm):
    class Meta:
        model= Animal
        fields = ('nome', 'pelagem', 'especie', 'tamanho', 'sexo', 'status', 'detalhes', 'imagem')