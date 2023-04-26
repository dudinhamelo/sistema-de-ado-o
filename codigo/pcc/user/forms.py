from django import forms 
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class AdicionarUser(UserCreationForm):
    class Meta(UserCreationForm):
        model= Usuario
        fields = ('username','first_name', 'last_name', 'email', 'telefone')
