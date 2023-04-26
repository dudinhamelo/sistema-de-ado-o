from django.urls import include, path
from . import views

urlpatterns = [
    path('cadastro/', views.Cadastrar.as_view(), name='Cadastrar'),
    path('', views.Home, name='Home'),
    path('tipo_de_cadastro/', views.TipoCadastro, name='TipoCadastro')
]