from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.Cadastro, name='Cadastro'),
    path('editar/<int:id_animal>', views.Editar, name='Editar'),
    path('listar/', views.Listar, name='Listar'),
    path('detalhar/<int:id_animal>', views.Detalhar, name='Detalhar'),
    path('detalhar-2/<int:id_animal>', views.Detalhar2, name='Detalhar2'),
    path('deletar/<int:id_animal>', views.Deletar, name='Deletar'),
    path('', views.ListarparaONG, name='ListarparaONG')
]