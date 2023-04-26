from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import Usuario
from ONG.models import ONG
from .forms import AdicionarUser

class Cadastrar(generic.CreateView):
    form_class = AdicionarUser
    template_name = 'Cadastrar.html'
    success_url = reverse_lazy('login')

@login_required
def Home(request):
   return redirect('/animais/listar/')

@login_required
def TipoCadastro(request):
    return render(request, 'TipoCadastro.html')