from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AdicionarAnimal
from .models import Animal
from ONG.models import ONG
from user.models import Usuario
import os 

@login_required
def Cadastro (request):
    if request.method =='POST':
        form = AdicionarAnimal(request.POST, request.FILES)
        u = request.user
        ong = get_object_or_404(ONG,user=u)
        if form.is_valid():
            a = form.save(commit=False)
            a.ong = ong
            a.save()
            return redirect('/accounts/')
    else:
        form = AdicionarAnimal()
    
    return render(request, 'Animal/Cadastro.html', {'form': form})

@login_required
def Editar(request, id_animal):
    animal= get_object_or_404(Animal, pk=id_animal)
    form = AdicionarAnimal(instance=animal)
    if request.method == 'POST':
        form = AdicionarAnimal(request.POST, request.FILES, instance=animal)
        
        requisicao = request.POST.get('imagem', False)
        if requisicao:
            if len(animal.imagem)>0:
                os.remove(animal.imagem.path)
            animal.imagem = request.FILES['imagem']


        if form.is_valid():
            form.save()
            return redirect('/accounts/')
        else:
            return render(request, 'Animal/Editar.html', {'form': form, 'animal': animal})   
    
    else:
        return render(request, 'Animal/Editar.html', {'form': form, 'animal':animal})

@login_required
def Listar(request):
    #u = request.Usuario
    #usuario_atual = get_object_or_404(Usuario, user=u)
    animais = Animal.objects.all()
    return render(request, 'Animal/Listar.html', {'animais': animais})

@login_required
def ListarparaONG(request):
    u = request.user
    o = get_object_or_404(ONG, user=u)
    animais = Animal.objects.filter(ong=o)
    return render(request, 'Animal/ListarONG.html', {'animais': animais, 'ong':o})

@login_required
def Detalhar(request, id_animal):
    animal = Animal.objects.get(pk=id_animal)
    return render(request, 'Animal/Detalhar.html', {'animal': animal})

@login_required
def Detalhar2(request, id_animal):
    animal = Animal.objects.get(pk=id_animal)
    return render(request, 'Animal/Detalhar2.html', {'animal': animal})

@login_required
def Deletar(request, id_animal):
    Animal.objects.get(pk=id_animal).delete()
    return redirect('/accounts/')

