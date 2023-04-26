from django.db import models
from django.contrib.auth import get_user_model


class ONG(models.Model):
    email = models.EmailField(max_length = 256, blank=False, null=True)
    nome = models.CharField(max_length = 100, blank=False, null=True)
    cidade = models.CharField(max_length=100, blank=False, null=True)
    UF = models.CharField(max_length=100, blank=False, null=True)
    rua = models.CharField(max_length=100, blank=False, null=True)
    numero = models.CharField(max_length=10, blank=False, null=True)
    bairro = models.CharField(max_length=100, blank=False, null=True)
    telefone = models.CharField(max_length=15, blank=False, null=True)
    imagem = models.ImageField(upload_to='static/imagens/ong/', null=True, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)