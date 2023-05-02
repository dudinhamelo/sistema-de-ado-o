from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import Usuario
from ONG.models import ONG
from .forms import AdicionarUser, ChangeUser

class Cadastrar(generic.CreateView):
    form_class = AdicionarUser
    template_name = 'Cadastrar.html'
    success_url = reverse_lazy('login')

@login_required
def Home(request):
    u = request.user
    ong = ONG.objects.filter(user=u)
    if u.choose_ong:
        if ong:
            return redirect('/animais/')
        else:
            return redirect('/animais/listar/')
    else:
        u.choose_ong = 'True'
        u.save()
        return redirect('/accounts/tipo_de_cadastro/')
   

@login_required
def TipoCadastro(request):
    return render(request, 'TipoCadastro.html')


@login_required
def Editar(request):
    u = request.user
    form = ChangeUser(instance=u)
    if request.method == 'POST':
        form = ChangeUser(request.POST, instance=u)

        if form.is_valid():
            form.save()
            return redirect('/accounts/')
        else:
            return render(request, 'Usuario/Editar.html', {'form': form, 'u': u})   
    
    else:
        return render(request, 'Usuario/Editar.html', {'form': form, 'u': u})


@login_required
def MeuPerfil(request):
    u = request.user
    return render(request, 'Usuario/Detalhar.html', {'u':u})