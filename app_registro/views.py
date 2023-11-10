from django.shortcuts import render
from .models import Topico,Entrada
from .forms import TopicoForm,EntradaForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'app_registro/index.html')

@login_required
def topicos(request):
    topicos = Topico.objects.filter(owner=request.user).order_by('data_edicao')
    context = {'topicos':topicos}
    return render(request, 'app_registro/topicos.html', context)

@login_required
def topico(request, topico_id):
    topico = Topico.objects.get(id=topico_id)
    if topico.owner != request.user:
        raise Http404
    
    entradas = topico.entrada_set.order_by('-data_edicao')
    context = {'topico':topico, 'entradas':entradas}
    return render(request, 'app_registro/topico.html',context)

@login_required
def novo_topico(request):
    if request.method != 'POST':
        form = TopicoForm()
    else:
        form = TopicoForm(request.POST)
        if form.is_valid():
            novo_topico = form.save(commit=False)
            novo_topico.owner = request.user
            novo_topico.save()
            return HttpResponseRedirect(reverse('app_registro:topicos'))
        
    context = {'form':form}
    return render(request, 'app_registro/novo_topico.html',context)

@login_required
def nova_entrada(request, topico_id):
    topico = Topico.objects.get(id=topico_id)
    if topico.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntradaForm()
    else:
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.topico = topico
            nova_entrada.save()
            return HttpResponseRedirect(reverse('app_registro:topico', args=[topico_id]))
    context = {'topico':topico, 'form':form}
    return render(request, 'app_registro/nova_entrada.html', context)

@login_required
def editar_entrada(request, entrada_id):
    entrada = Entrada.objects.get(id=entrada_id)
    topico = entrada.topico
    if topico.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntradaForm(instance=entrada)
    else:
        form = EntradaForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_registro:topico', args=[topico.id]))
    contexto = {'entrada':entrada, 'topico':topico, 'form':form}
    return render(request, 'app_registro/editar_entrada.html', contexto)