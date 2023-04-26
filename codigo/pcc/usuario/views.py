from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AdicionarUsuario 
from .models import Usuario
import os

@login_required
def Cadastro (request):
    if request.method =='POST':
        form = AdicionarUsuario(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('/accounts/')
    else:
        form = AdicionarUsuario()
    
    return render(request, 'Usuario/Cadastro.html', {'form': form})

@login_required
def Editar(request):
    u = request.user
    usuario= get_object_or_404(Usuario, user=u)
    form = AdicionarUsuario(instance=usuario)
    if request.method == 'POST':
        form = AdicionarUsuario(request.POST, request.FILES, instance=usuario)

        requisicao = request.POST.get('imagem', False)
        if requisicao:
            if len(usuario.imagem)>0:
                os.remove(usuario.imagem.path)
            usuario.imagem = request.FILES['imagem']

        if form.is_valid():
            form.save()
            return redirect('/accounts/')
        else:
            return render(request, 'Usuario/Editar.html', {'form': form, 'usuario': usuario})   
    
    else:
        return render(request, 'Usuario/Editar.html', {'form': form, 'usuario': usuario})

@login_required
def Listar(request):
    usuarios = Usuario.objects.all()
    return render(request, 'Usuario/Listar.html', {'usuarios': usuarios})

@login_required
def MeuPerfil(request):
    u = request.user
    usuario = Usuario.objects.get(user=u)
    return render(request, 'Usuario/Detalhar.html', {'usuario': usuario})