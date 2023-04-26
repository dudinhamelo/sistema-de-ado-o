from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.Cadastro, name='Cadastro'),
    path('editar/', views.Editar, name='Editar'),
    path('listar/', views.Listar, name='Listar'),
    path('meu-perfil/', views.MeuPerfil, name='MeuPerfil')
]