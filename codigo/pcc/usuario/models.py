from django.db import models
from django.contrib.auth import get_user_model


class Usuario(models.Model):
    email = models.EmailField(max_length = 256, blank=False, null=True)
    nome = models.CharField(max_length = 100, blank=False, null=True)
    sobrenome = models.CharField(max_length=100, blank=False, null=True)
    telefone = models.CharField(max_length=15, blank=False, null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='static/imagens/perfil/', null=True, blank=True)

