from django.shortcuts import render 
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_registro:index'))

def registro(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            usuario_autenticado = authenticate(username=novo_usuario.username, password = request.POST['password1'])
            login(request, usuario_autenticado)
            return HttpResponseRedirect(reverse('app_usuarios:login'))
    
    context = {'form':form} 
    return render(request, 'app_usuarios/registro.html', context)  