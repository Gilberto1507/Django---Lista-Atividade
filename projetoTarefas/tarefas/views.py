from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "lista.html", {"tarefas": tarefas})

def nova_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    
    return render(request, "formulario.html", {"form": form})

def detalhe_tarefa(request, pk):
    # Procura a tarefa pelo número (pk). Se não existir, mostra erro 404
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, "detalhe.html", {"tarefa": tarefa})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == "POST":
        # O instance=tarefa avisa o formulário para atualizar esta tarefa, e não criar uma nova
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('detalhe_tarefa', pk=tarefa.pk)
    else:
        # Carrega o formulário já preenchido com os dados atuais
        form = TarefaForm(instance=tarefa)
        
    return render(request, "formulario.html", {"form": form})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == "POST":
        tarefa.delete() # Comando que apaga a tarefa da base de dados
        return redirect('lista_tarefas')
        
    return render(request, "confirmar_exclusao.html", {"tarefa": tarefa})

def alternar_status(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    # Inverte o valor atual (se for True vira False, se for False vira True)
    tarefa.concluida = not tarefa.concluida 
    tarefa.save() # Guarda a alteração na base de dados
    
    # Redireciona de volta para a página de detalhes dessa mesma tarefa
    return redirect('detalhe_tarefa', pk=tarefa.pk)