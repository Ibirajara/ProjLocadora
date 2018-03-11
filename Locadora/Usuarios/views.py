from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios
from .forms import UsuarioForm
# Create your views here.

def listarUsuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'listar.html', {'usuarios': usuarios})

def incluirUsuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'formUsuario.html', {'form': form})

def atualizarUsuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    form = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'formUsuario.html', {'form': form})

def deletarUsuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    form = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        return redirect('listar')
    return render(request, 'confirmaDeletar.html', {'usuario': usuario})