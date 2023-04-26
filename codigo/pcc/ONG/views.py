from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AdicionarONG
from .models import ONG
import os

@login_required
def Cadastro (request):
    if request.method =='POST':
        form = AdicionarONG(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('/accounts/')
    else:
        form = AdicionarONG()
    
    return render(request, 'ONG/Cadastro.html', {'form': form})

@login_required
def Editar(request):
    usuario = request.user
    ong = get_object_or_404(ONG, user=usuario)
    form = AdicionarONG(instance=ong)
    if request.method == 'POST':
        form = AdicionarONG(request.POST, request.FILES, instance=ong)

        requisicao = request.POST.get('imagem', False)
        if requisicao:
            if len(ong.imagem)>0:
                os.remove(ong.imagem.path)
            ong.imagem = request.FILES['imagem']

        if form.is_valid():
            form.save()
            return redirect('/accounts/')
        else:
            return render(request, 'ONG/Editar.html', {'form': form, 'ong':ong})   
    
    else:
        return render(request, 'ONG/Editar.html', {'form': form, 'ong':ong})

@login_required
def Listar(request):
    ongs = ONG.objects.all()
    return render(request, 'ONG/Listar.html', {'ongs': ongs})

@login_required
def Detalhar(request, id_ong):
    ong = ONG.objects.get(pk=id_ong)
    return render(request, 'ONG/Detalhar.html', {'ong': ong})

@login_required
def MeuPerfil(request):
    u = request.user
    ong = ONG.objects.get(user=u)
    return render(request, 'ONG/MeuPerfil.html', {'ong': ong})
