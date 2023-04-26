from django.db import models
from ONG.models import ONG

class Animal(models.Model):
    nome = models.CharField(max_length = 100, blank=False, null=True)
    pelagem = models.CharField(max_length=100, blank=False, null=True)
    especie = models.CharField(max_length=100, blank=False, null=True)
    tamanho = models.CharField(max_length=100, blank=False, null=True)
    Sexo_animal = (
        ('M', 'Macho'),
        ('F', 'Fêmea')
    )
    sexo = models.CharField(max_length=10, choices=Sexo_animal)
    Status_animal = (
        ('Adotado', 'Adotado'),
        ('Nao_adotado', 'Não Adotado')
    )
    status = models.CharField(max_length=50, choices=Status_animal)
    detalhes = models.TextField(max_length=10000, blank=True, null=True)
    imagem = models.ImageField(upload_to='static/imagens/animal/', null=True, blank=False)
    ong = models.ForeignKey(ONG, on_delete=models.PROTECT, related_name='ONG')